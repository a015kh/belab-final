#include <math.h>

int delay_time = 3;
const int analogInPin = A5;
int num_record = 30;
float history[30];
int count = 0;  
float total = 0;
float mean = 0;
float stddev = 0;
float max_err = 0;
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
  for(int i=0; i < num_record; i++) {
    float err = fabs(history[i] - mean);
    if err > max_err {
      max_err = err;
    }
  }
  max_err = 0;
  total = 0;
  max_err = 0;
  if (Serial.available() > 0) {
    Serial.read();
    Serial.println(max_err);
  }
  delay(delay_time);
}
