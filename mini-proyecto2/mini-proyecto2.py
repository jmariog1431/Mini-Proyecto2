import cv2
import mediapipe as mp
import serial
import sys
import math
import time


try:
    arduino = serial.Serial('COM4', 9600)  
    time.sleep(2)  
    print("[INFO] Conectado a Arduino.")
except serial.SerialException:
    print("[ERROR] No se pudo conectar a Arduino.")
    sys.exit(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
ultimo_numero = -1

def calcular_angulo(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) -
                       math.atan2(a[1] - b[1], a[0] - b[0]))
    ang = abs(ang)
    return 360 - ang if ang > 180 else ang

def contar_dedos(puntos):
    dedos = []

    angulo_pulgar = calcular_angulo(puntos[2], puntos[3], puntos[4])
    dedos.append(1 if angulo_pulgar > 150 else 0)

    for tip_id in [8, 12, 16, 20]:
        base_id = tip_id - 2
        angulo = calcular_angulo(puntos[base_id - 1], puntos[base_id], puntos[tip_id])
        dedos.append(1 if angulo > 160 else 0)

    return sum(dedos)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    dedos_contados = 0

    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        h, w, _ = frame.shape
        puntos = [(int(lm.x * w), int(lm.y * h)) for lm in handLms.landmark]
        dedos_contados = contar_dedos(puntos)
        dedos_contados = min(dedos_contados, 5)

    if dedos_contados != ultimo_numero:
        print(f"[INFO] Dedos detectados: {dedos_contados}")
        arduino.write(str(dedos_contados).encode())
        ultimo_numero = dedos_contados

    cv2.putText(frame, f"Dedos: {dedos_contados}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    cv2.imshow("Contador de Dedos", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
