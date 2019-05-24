#include "display.h"
#include "driverlib/rom_map.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Variable declaration
int PIRValue = 0;
int count = 0;
char buffer1[16], buffer2[16];
int time;
char value[16] = "Count: ";

int main()

{
    volatile uint32_t ui32Loop;

    //Peripheral and GPIO Initialization
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOB);
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, GPIO_PIN_3);
    GPIOPinTypeGPIOInput(GPIO_PORTB_BASE, GPIO_PIN_0);

    //Clock Initialization
    SysCtlClockSet(SYSCTL_SYSDIV_8|SYSCTL_USE_PLL|SYSCTL_XTAL_16MHZ|SYSCTL_OSC_MAIN);
    //LCD Initialization
    initLCD();

    while(1)
         {
             PIRValue = GPIOPinRead(GPIO_PORTB_BASE, GPIO_PIN_0);
             if(PIRValue == 1)
             {
                 // Displaying the people count
                 count++;
                 char value[16] = "Count: ";
                 ltoa(count, buffer1);
                 strcat(value, buffer1);
                 PIRValue = GPIOPinRead(GPIO_PORTB_BASE, GPIO_PIN_0);
                 GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_3, GPIO_PIN_3);
                 clearLCD();
                 printLCD(value);

                 //Infinite loop to check when the sensor output turns off
                 while( PIRValue == 1){
                     //Up-time calculation
                     PIRValue = GPIOPinRead(GPIO_PORTB_BASE, GPIO_PIN_0);
                     SysCtlDelay(SysCtlClockGet()/3);
                     time++;
                 }

                 //Displaying of the time calculated before
                 GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_3, 0x0);
                 char timeTag[16] = "Time: ";
                 ltoa(time, buffer2);
                 strcat(timeTag, buffer2);
                 clearLCD();
                 printLCD(timeTag);
                 time = 0;
                 SysCtlDelay(SysCtlClockGet()/3);
             }
             else
             {
                 //Resetting
                 GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_3, 0x0);
                 clearLCD();
             }
         }

}
