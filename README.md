# Mini-Proyecto2

El proyecto consiste en un sistema que cuenta los dedos levantados (de 0 a 5) utilizando visión por computadora. El número detectado se envía al Arduino a través de comunicación serial, donde se representa físicamente en un display de 7 segmentos conectado al arduino.

# Funcionamiento general:

Se usa Python con las librerías MediaPipe y OpenCV para detectar la mano y contar los dedos en tiempo real desde una cámara web.

Cada vez que cambia el número de dedos detectados, se envía el número al Arduino mediante comunicación serial USB.

El Arduino recibe el número y lo muestra usando un display de 7 segmentos.

Se comparte el link del video demostrativo: https://mega.nz/file/58hWFDYL#7r0Kfy528Ra6DvNvn899QG1AhdBDx4O8R9o-XklMxa0
