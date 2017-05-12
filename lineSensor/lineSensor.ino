#define enc_out 3
#define front_line_1 4
#define front_line_2 5
#define front_line_3 5
#define front_line_4 6

#define side_line_1 7
#define side_line_2 8
#define side_line_3 9

#define enc_count_amount 100

int current_line,side_line;
int line_pins[13] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12};
int values[13];
int enc, enc_amount;
int thresholds[9]={700,700,700,700,700,700,700,700,700};
void setup() {
  // front line sensors
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);
  pinMode(A8, INPUT);

  // side line sensors
  pinMode(A9, INPUT);
  pinMode(A10, INPUT);
  pinMode(A11, INPUT);
  pinMode(A12, INPUT);

  // encoder
  pinMode(2, INPUT_PULLUP);

  Serial.begin(115200);
  for (int i = 0; i < 13; i++)
    values[i] = 0;

  enc = enc_amount = 0;
}

void loop() {

  for (int i = 0; i < 5; i++) {
    values[0] += analogRead(line_pins[0]);
    values[1] += analogRead(line_pins[1]);
    values[2] += analogRead(line_pins[2]);
    values[3] += analogRead(line_pins[3]);
    values[4] += analogRead(line_pins[4]);
    values[5] += analogRead(line_pins[5]);
    values[6] += analogRead(line_pins[6]);
    values[7] += analogRead(line_pins[7]);
    values[8] += analogRead(line_pins[8]);
    values[9] += analogRead(line_pins[9]);
    values[10] += analogRead(line_pins[10]);
    values[11] += analogRead(line_pins[11]);
    values[12] += analogRead(line_pins[12]);
  }

  for (int i = 0; i < 5; i++) {
    values[0] /= 5;
    values[1] /= 5;
    values[2] /= 5;
    values[3] /= 5;
    values[4] /= 5;
    values[5] /= 5;
    values[6] /= 5;
    values[7] /= 5;
    values[8] /= 5;
    values[9] /= 5;
    values[10] /= 5;
    values[11] /= 5;
    values[12] /= 5;
  }

  enc += digitalRead(2);
  if (++enc_amount == enc_count_amount) {
    if (enc < enc_count_amount / 2)
      digitalWrite(enc_out, LOW);
    else
      digitalWrite(enc_out, HIGH);
    enc = 0;
  }

  // encode front line; 1 far left, 9 far right, 5 mid
  compute_front_line();
  switch (current_line)
  {
    case 0: //no line detected
      digitalWrite(front_line_1, LOW);
      digitalWrite(front_line_2, LOW);
      digitalWrite(front_line_3, LOW);
      digitalWrite(front_line_4, LOW);
      break;
    case 1:
      digitalWrite(front_line_1, HIGH);
      digitalWrite(front_line_2, LOW);
      digitalWrite(front_line_3, LOW);
      digitalWrite(front_line_4, LOW);
      break;
    case 2:
      digitalWrite(front_line_1, LOW);
      digitalWrite(front_line_2, HIGH);
      digitalWrite(front_line_3, LOW);
      digitalWrite(front_line_4, LOW);
      break;
    case 3:
      digitalWrite(front_line_1, HIGH);
      digitalWrite(front_line_2, HIGH);
      digitalWrite(front_line_3, LOW);
      digitalWrite(front_line_4, LOW);
      break;
    case 4:
      digitalWrite(front_line_1, LOW);
      digitalWrite(front_line_2, LOW);
      digitalWrite(front_line_3, HIGH);
      digitalWrite(front_line_4, LOW);
      break;
    case 5:
      digitalWrite(front_line_1, HIGH);
      digitalWrite(front_line_2, LOW);
      digitalWrite(front_line_3, HIGH);
      digitalWrite(front_line_4, LOW);
      break;
    case 6:
      digitalWrite(front_line_1, LOW);
      digitalWrite(front_line_2, HIGH);
      digitalWrite(front_line_3, HIGH);
      digitalWrite(front_line_4, LOW);
      break;
    case 7:
      digitalWrite(front_line_1, HIGH);
      digitalWrite(front_line_2, HIGH);
      digitalWrite(front_line_3, HIGH);
      digitalWrite(front_line_4, LOW);
      break;
    case 8:
      digitalWrite(front_line_1, LOW);
      digitalWrite(front_line_2, LOW);
      digitalWrite(front_line_3, LOW);
      digitalWrite(front_line_4, HIGH);
      break;
    case 9:
      digitalWrite(front_line_1, HIGH);
      digitalWrite(front_line_2, LOW);
      digitalWrite(front_line_3, LOW);
      digitalWrite(front_line_4, HIGH);
      break;
  }

  //encode side lines
  compute_side_line();
  switch (side_line)
  {
    case 0: // no line detected
      digitalWrite(side_line_1, LOW);
      digitalWrite(side_line_2, LOW);
      digitalWrite(side_line_3, LOW);
      break;
    case 1: // front left detected
      digitalWrite(side_line_1, LOW);
      digitalWrite(side_line_2, LOW);
      digitalWrite(side_line_3, HIGH);
      break;
    case 2: // front right detected
      digitalWrite(side_line_1, HIGH);
      digitalWrite(side_line_2, LOW);
      digitalWrite(side_line_3, HIGH);
      break;
    case 3: // back left detected
      digitalWrite(side_line_1, LOW);
      digitalWrite(side_line_2, HIGH);
      digitalWrite(side_line_3, HIGH);
      break;
    case 4: // back right detected
      digitalWrite(side_line_1, HIGH);
      digitalWrite(side_line_2, HIGH);
      digitalWrite(side_line_3, HIGH);
      break;

  }

  /*
    printInt(analogRead(A0));
    Serial.print(" | ");
    printInt(analogRead(A1));
    Serial.print(" | ");
    printInt(analogRead(A2));
    Serial.print(" | ");
    printInt(analogRead(A3));
    Serial.print(" | ");
    printInt(analogRead(A4));
    Serial.print(" | ");
    printInt(analogRead(A5));
    Serial.print(" | ");
    printInt(analogRead(A6));
    Serial.print(" | ");
    printInt(analogRead(A7));
    Serial.print(" | ");
    printInt(analogRead(A8));
    Serial.println();
  */
  delay(10);

}
void printInt(int a)
{
  if (a < 10)
    Serial.print("000");
  else if (a < 100)
    Serial.print("00");
  else if (a < 1000)
    Serial.print("0");
  Serial.print(a);
}

void compute_front_line()
{
  bool all_0 = true;
  for (int i = 0; i < 9; i++)
    if (values[i] < 750)
      all_0 = false;

  if (all_0)
    current_line = 0;
  else
  { 
    int between=0;
    for(int i=0;i<8;i++)
      {
        if(values[i]<thresholds[i] &&values[i+1]<thresholds[i+1]) //check if line between two sensors
          {
            current_line=10+i; 
            between=1;
            break;
          }
      }
    if(! between)
    {
     if (values[0] < 700)
      current_line = 1;
    else if (values[1] < 700)
      current_line = 2;
    else if (values[2] < 700)
      current_line = 3;
    else if (values[3] < 700)
      current_line = 4;
    else if (values[4] < 700)
      current_line = 5;
    else if (values[5] < 700)
      current_line = 6;
    else if (values[6] < 700)
      current_line = 7;
    else if (values[7] < 700)
      current_line = 8;
    else if (values[8] < 700)
      current_line = 9;
  }
  }
}

void compute_side_line()
{
  bool all_0 = true;
  for (int i = 9; i < 13; i++)
    if (values[i] < 750)
      all_0 = false;

  if (all_0)
    side_line = 0;
  else
  {
    if(values[9]<700 and values[10])
      side_line=5;
     else if(values[11]<700 and values[12]<700)
        side_line=6;
    else if (values[9] < 700)
      side_line = 1;
    else if (values[10] < 700)
      side_line = 2;
    else if (values[11] < 700)
      side_line = 3;
    else if (values[12] < 700)
      side_line = 4;
  }
  

}

