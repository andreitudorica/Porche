#define nr_front_sensors 9
int front_sensors[nr_front_sensors]={A0,A1,A2,A3,A4,A5,A6,A7,A8};
int front_binary[5]={7,8,9,10,11};
int nr_samples=10000;
long long  sensors_sum[nr_front_sensors];
double sensors_average[nr_front_sensors];

void setup() {
  Serial.begin(115200);
  for(int i=0; i<nr_front_sensors ;i++)
  {
    pinMode(front_sensors[i],INPUT);
  }
   for(int i=0; i<5 ;i++)
  {
    pinMode(front_binary[i],OUTPUT);
  }
  
  
  for(int i=0;i<nr_samples;i++)
  {
    for(int j=0;j<nr_front_sensors;j++)
      {
        sensors_sum[j]+=analogRead(front_sensors[j]);
      }
    
  }
   for(int j=0;j<nr_front_sensors;j++)
      {
        sensors_average[j]=sensors_sum[j]/nr_samples;
      }
  Serial.print("Started");
}
void set_front_binary(int value)
{
  for(int i=0;i<5;i++)
  {
    if(value%2==1)
      digitalWrite(front_binary[i],HIGH);
    else
      digitalWrite(front_binary[i],LOW);
      value=value/2;
  }
  
}
void loop() {
  
  analogWrite(13,255);
  double min=32000;;
  int sensor_triggered=-1;
  double value=33;
  for(int j=0;j<nr_front_sensors;j++)
  {
    value=analogRead(front_sensors[j])/sensors_average[j];
    if(value<min&&value <0.85)
      {
        min=value;
        sensor_triggered=j;
      }
   
  }
if(min!=32000)
{
  set_front_binary(sensor_triggered+1);
   Serial.print(sensor_triggered+1);
 Serial.print(" ");
  Serial.print(min);

  Serial.println();
}
else
{
  set_front_binary(0);
}

// for(int j=0;j<nr_front_sensors;j++)
//  {
//    Serial.print(sensors_average[j]);
//    Serial.print(" ");
//  }
 
//delay(50);
  

}
