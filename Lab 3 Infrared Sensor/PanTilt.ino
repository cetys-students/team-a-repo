#include <Servo.h>

int Up_Sensor = 3;
int Right_Sensor = 4;
int Down_Sensor = 5;
int Left_Sensor = 6;
int pos = 1472;
int angleS = 1;
int angleI = 1;

Servo servoTop;     //initialize a servo object for the connected servo
Servo servoBottom;

void setup() {
  Serial.begin(9600);
  //sensors
  pinMode(Up_Sensor, INPUT);
  pinMode(Right_Sensor, INPUT);
  pinMode(Down_Sensor, INPUT);
  pinMode(Left_Sensor, INPUT);
  //motors
  servoTop.attach(9);
  servoTop.write(1);
  servoBottom.attach(10);
  servoBottom.write(1);
}

void loop() {
  
  //Read sensors
  int Up = digitalRead(Up_Sensor);
  int Right = digitalRead(Right_Sensor);
  int Down = digitalRead(Down_Sensor);
  int Left = digitalRead(Left_Sensor);
  Serial.print("Up= ");
  Serial.print(Up);
  Serial.print(" ");
  Serial.print("Right= ");
  Serial.print(Right);
  Serial.print(" ");
  Serial.print("Down= ");
  Serial.print(Down);
  Serial.print(" ");
  Serial.print("Left= ");
  Serial.print(Left);
  Serial.println(" ");
  
  //Move motors accordingly
  //Check if we have all 0s or 1s
  if(Up==0)
  {  
    angleS+=5;
    servoTop.write(angleS);   
  }
  
  if(Down == 0)
  {
    angleS-=5;
    servoTop.write(angleS);
  }

  if(Right == 0)
  {
    angleI-=5;
    servoBottom.write(angleI);
  }
  
  if(Left == 0)
  {
    angleI+=5;
    servoBottom.write(angleI);
  }
  
  //Check if we have pairs

  //Check if we have singles
  
  delay(90);
}
