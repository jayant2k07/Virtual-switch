const int led1 = 8;
const int led2 = 9;
const int led3 = 10;

bool state1 = false;
bool state2 = false;
bool state3 = false;

void setup() {
  Serial.begin(9600);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {

    char data = Serial.read();

    if (data == '1') {
      state1 = !state1;
      digitalWrite(led1, state1);
    }

    if (data == '2') {
      state2 = !state2;
      digitalWrite(led2, state2);
    }

    if (data == '3') {
      state3 = !state3;
      digitalWrite(led3, state3);
    }
  }
}