#include <Stepper.h>

long distance;
long TotalTime;
int value;
int in1Pin = 8;
int in2Pin = 9;
int in3Pin = 10;
int in4Pin = 11;
int stepcount = 0;
const int StepPerRevolution = 200;
int FinalStepCount = 0;
int FinalDistance = 0;
int push1 = A2;
int push2 = A1;

Stepper stepper(StepPerRevolution, in1Pin, in2Pin, in3Pin, in4Pin);

void setup(){
      Serial.begin(9600);
      pinMode(6, OUTPUT); 
      pinMode(12, INPUT); 
      pinMode(push1,INPUT);
      pinMode(push2,INPUT);
      pinMode(in1Pin, OUTPUT);
      pinMode(in2Pin, OUTPUT);
      pinMode(in3Pin, OUTPUT);
      pinMode(in4Pin, OUTPUT);
}

void loop() {
      int botton1 = digitalRead(push1);
      Serial.println(botton1);
      
      if(botton1 == 1)
      {
        lap();
      }
      
      delay(50);
  
}

void lap(){
      int botton2 = digitalRead(push2);
          do{
                if(botton2 == 1)
                {
                    Serial.println("bye");
                    break;
                }
                
                int input = digitalRead(push1);
                Serial.println(input);
                stepper.setSpeed(50);
                stepper.step(100);
                digitalWrite(6,LOW); 
                delayMicroseconds(5);
                digitalWrite(6, HIGH); 
                delayMicroseconds(10);
                TotalTime=pulseIn(12, HIGH); 
                distance= int(0.017*TotalTime);
                
                if(stepcount == 0)
                {
                      FinalDistance = distance;
                }
                
                if(distance<FinalDistance)
                {
                      FinalDistance = distance;
                      FinalStepCount = stepcount;
                }
                
                Serial.println("Distance ");
                Serial.print(distance);
                Serial.println(" cm");
                stepcount++;
                delay(50);
          
           }
           
      while(stepcount<StepPerRevolution);
      stepper.step(FinalStepCount);
  }
  
  
