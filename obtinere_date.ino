
#include <SparkFun_ADXL345.h>
ADXL345 adxl = ADXL345();

int ledPin = 13; 
int digitalPin = 2; 
int analogPin = A0;
int digitalVal;
int analogVal;
int range = 2
void setup() {
  Serial.begin(19200);
  pinMode(ledPin, OUTPUT); 
  pinMode(digitalPin, INPUT); 
  adxl.powerOn();
  adxl.setRangeSetting(2);
}

void loop() {

  digitalVal = digitalRead(digitalPin);

  analogVal = analogRead(analogPin);


  Serial.println(" A: ");
  
  // Calibration
  Serial.println(analogVal - 521); 
  
  int x, y, z;
  adxl.readAccel(&x, &y, &z);

  // Calibration  -1000 < x, y, z < 1000
     
      x = x * 3.9;
      y = y * 3.9;
      z = z * 3.9;
   
  Serial.print(" X: ");
  Serial.print(x);

  Serial.print(" Y: ");
  Serial.print(y);

  Serial.print(" Z: ");
  Serial.println(z);
  // Serial.println(millis());
}


