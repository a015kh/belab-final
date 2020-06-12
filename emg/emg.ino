int delay_time = 30;
const int analogInPin = A5;


void setup() {
  Serial.begin(9600);
}
 
void loop() {
  int sensorValue = analogRead(analogInPin);
  Serial.println(sensorValue);
  delay(delay_time);
}
