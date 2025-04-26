int a = 2; 
int b = 3;
int c = 4;
int d = 5;
int e = 6;
int f = 7;
int g = 8;

byte numeros[6][7] = {
  {0, 0, 0, 0, 0, 0, 1}, // 0
  {1, 0, 0, 1, 1, 1, 1}, // 1
  {0, 0, 1, 0, 0, 1, 0}, // 2
  {0, 0, 0, 0, 1, 1, 0}, // 3
  {1, 0, 0, 1, 1, 0, 0}, // 4
  {0, 1, 0, 0, 1, 0, 0}  // 5
};

void setup() {
  for (int i = 2; i <= 8; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH); 
  }

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();

    if (c >= '0' && c <= '5') {
      int n = c - '0';
      mostrarNumero(n);
    }
  }
}

void mostrarNumero(int numero) {
  digitalWrite(a, numeros[numero][0]);
  digitalWrite(b, numeros[numero][1]);
  digitalWrite(c, numeros[numero][2]);
  digitalWrite(d, numeros[numero][3]);
  digitalWrite(e, numeros[numero][4]);
  digitalWrite(f, numeros[numero][5]);
  digitalWrite(g, numeros[numero][6]);
}
