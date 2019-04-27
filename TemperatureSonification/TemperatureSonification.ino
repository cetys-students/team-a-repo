
int frequencies[] = {262, 294, 330, 349, 392, 440, 493, 523, 587, 659};
const int Buzz = 10;
int newValue;
int sensorValue;
int Temp;
int rounded;

 void buzz(int Temp){
  if (Temp <= 10){
    tone(Buzz,frequencies[0]);
    Serial.println("C");
  }
   if ((Temp >= 11)&&(Temp <= 20) ){
    tone(Buzz,frequencies[1]);
    Serial.println("D");
  }
  if ((Temp >= 21)&&(Temp <= 30) ){
    tone(Buzz,frequencies[2]);
    Serial.println("E");
  }
  if ((Temp >= 31)&&(Temp <= 40) ){
    tone(Buzz,frequencies[3]);
    Serial.println("F");
  }
  if ((Temp >= 41)&&(Temp <= 50) ){
    tone(Buzz,frequencies[4]);
    Serial.println("G");
  }
  if ((Temp >= 51)&&(Temp <= 60) ){
    tone(Buzz,frequencies[5]);
    Serial.println("A");
  }
  if ((Temp >= 61)&&(Temp <= 70) ){
    tone(Buzz,frequencies[6]);
    Serial.println("B");
  }
  if ((Temp >= 71)&&(Temp <= 80) ){
    tone(Buzz,frequencies[7]);
    Serial.println("C2");
  }
  if ((Temp >= 81)&&(Temp <= 90) ){
    tone(Buzz,frequencies[8]);
    Serial.println("B2");
  }
  if (Temp >= 91){
    tone(Buzz,frequencies[9]);
    Serial.println("A ");
    Serial.println("Maximum Temperature!");
  }
  
  }


void setup() {
  Serial.begin(9600);
  int sensorValue = (analogRead(A0))*.5;
  Serial.println("Initial Read: ");
  Serial.print(sensorValue);
  Serial.println("C");
  buzz(sensorValue);
  delay(1000);
  noTone(Buzz);
}


void loop() {
  
  int sensorValue = (analogRead(A0))*.5;
  rounded = 10* round(sensorValue/10.0);
  sensorValue = rounded;
  delay(1500);
  int newValue = (analogRead(A0))*.5;
  rounded = 10* round(newValue/10.0);
  newValue = rounded;
  int difference = newValue - sensorValue;
  difference = abs(difference);
  Serial.print("The difference is: ");
  Serial.print(difference);
  Serial.print("    The temperature is: ");
  Serial.println((analogRead(A0))*.5);
  if (difference >= 10){
    buzz(newValue);
    delay(1000);
    noTone(Buzz);
    
  }
  
  
}
