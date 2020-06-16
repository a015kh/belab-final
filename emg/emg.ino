#include <math.h>

int delay_time = 3;
const int analogInPin = A5;
int num_record = 100;
float history[100];
int count = 0;  
float total = 0;
float mean = 0;
float stddev = 0;
float mean_err = 0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(analogInPin);
  int index = count % num_record;
  history[index] = sensorValue;
  count += 1;
  for(int i=0; i<num_record; i++) {
    total += history[i];
  }
  mean = total / num_record;
  total = 0;
  for(int i=0; i < num_record; i++) {
    float err = fabs(history[i] - mean);
    total += err;
  }
  mean_err = total / num_record;
  if (Serial.available() > 0) {
    Serial.read();
    Serial.println(mean_err);
    Serial.flush();
  }
  mean_err = 0;
  total = 0;
  delay(delay_time);
}
