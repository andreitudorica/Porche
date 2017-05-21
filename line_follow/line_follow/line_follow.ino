#include "LiquidCrystal.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_TSL2561_U.h>
#include <Servo.h>
Servo dir;
Servo throttle;
long sensors[] = { 0,0,0,0,0,0,0,0,0 };
long sensors_average;
int sensors_sum;
int position;

void setup() {
	
}
void loop() {

	sensors_average = 0;
	sensors_sum = 0;

	int min = 10000;
	int poz = 0;
	for (int i = 0; i < 8; i++)
	{
		sensors[i] = analogRead(i);
		if (sensors[i] < min)
		{
			min = sensors[i];
			poz = i;
		}
		sensors_average += sensors[i] * i * 1000;   //Calculating the weighted mean
		sensors_sum += int(sensors[i]);
	}
	position = int(sensors_average / sensors_sum);
	Serial.println(position);
	delay(100);
}

void pid_calc() {
	position = int(sensors_average / sensors_sum);
	/*
	proportional = position – set_point;      // Replace set_point by your set point
	integral = integral + proportional;
	derivative = proportional - last_proportional;
	last_proportional = proportional;

	error_value = int(proportional * Kp + integral * Ki + derivative * Kd);*/
}