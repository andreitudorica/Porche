#include "LiquidCrystal.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_TSL2561_U.h>
#include <Servo.h>
Servo dir;
Servo throttle;
int where_am_i = 0; //  -1 is too far left, 1 is too far right, 0 is ok
int car_direction = 90;
int car_throttle = 98;
int s1_val, s2_val, s3_val;
long long last_millis = 0;
long long last_millis_2 = 0;
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(52, 50, 48, 46, 44, 42);

Adafruit_TSL2561_Unified tsl1 = Adafruit_TSL2561_Unified(TSL2561_ADDR_LOW, 1);
Adafruit_TSL2561_Unified tsl2 = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 2);
Adafruit_TSL2561_Unified tsl3 = Adafruit_TSL2561_Unified(TSL2561_ADDR_HIGH, 3);
void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  tsl1.setGain(TSL2561_GAIN_16X);
  tsl1.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);
  if (!tsl1.begin())
  {
    lcd.print("S1 error");
    while (1);
  }
  tsl2.setGain(TSL2561_GAIN_16X);
  tsl2.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);
  if (!tsl2.begin())
  {
    lcd.print("S2 error");
    while (1);
  }
  tsl3.setGain(TSL2561_GAIN_16X);
  tsl3.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);
  if (!tsl3.begin())
  {
    lcd.print("S3 error");
    while (1);
  }

  lcd.setCursor(0, 0);
  lcd.print("S1");
  lcd.setCursor(6, 0);
  lcd.print("S2");
  lcd.setCursor(12, 0);
  lcd.print("S3");

  dir.attach(2);
  throttle.attach(3);
  throttle.write(90);
  delay(3000);
}
void loop() {
  sensors_event_t event1;
  sensors_event_t event2;
  sensors_event_t event3;
  tsl1.getEvent(&event1);
  tsl2.getEvent(&event2);
  tsl3.getEvent(&event3);

  if (millis() - last_millis > 1000) {
    lcd.setCursor(0, 1);
    lcd.print("                ");
    lcd.setCursor(0, 1);
    lcd.print((int)event1.light);
    lcd.setCursor(6, 1);
    lcd.print((int)event2.light);
    lcd.setCursor(12, 2);
    lcd.print((int)event3.light);
    last_millis = millis();
  }

  s1_val = event3.light;
  s2_val = event2.light;
  s3_val = event1.light;
  int s_min = min(s1_val, s2_val);
  s_min = min(s_min, s3_val);

  if ((s1_val <= s_min + 10) && (s2_val <= s_min + 10) && (s3_val <= s_min + 10)) {
    if (millis() - last_millis_2 > 700) {
      where_am_i = 2;
    }
  }
  else
  {
    last_millis_2 = millis();
    s1_val -= s_min;
    s2_val -= s_min;
    s3_val -= s_min;
    if (s1_val == 0) {
      where_am_i = -1;
    }
    if (s2_val == 0) {
      where_am_i = 0;
    }
    if (s3_val == 0) {
      where_am_i = 1;
    }
  }


  switch (where_am_i) {
    case -1:
      if (car_direction <= 115) car_direction += 5;
      //car_direction = 115;
      delay(30);
      car_throttle = 98;
      break;
    case 0:
      car_direction = 90;
      car_throttle = 98;
      break;
    case 1:
      if (car_direction >= 65) car_direction -= 5;
      delay(30);
      //car_direction = 65;
      car_throttle = 98;
      break;
    default: car_throttle = 90;
  }

  dir.write(car_direction);
  throttle.write(car_throttle);

}
