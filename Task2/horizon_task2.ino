#include <Servo.h>

Servo servoMotor;   // servo object

// pin setup
const int potPin = A0;
const int servoPin = 9;
const int ledPin = 13;

void setup() {
  servoMotor.attach(servoPin);   // connect servo
  pinMode(ledPin, OUTPUT);       // LED as output
}

void loop() {

  int potVal = analogRead(potPin);   // read analog value (0–1023)

  // convert it to servo angle
  int requested_angle = map(potVal, 0, 1023, 0, 180);

  // limit the movement to avoid going beyond 68°
  if (requested_angle > 68) {
    servoMotor.write(68);       // stop at max safe angle
    digitalWrite(ledPin, HIGH); // indicate limit reached
  } 
  else {
    servoMotor.write(requested_angle);    // normal movement
    digitalWrite(ledPin, LOW);  // LED off
  }

  delay(15);  // small pause for stability
}