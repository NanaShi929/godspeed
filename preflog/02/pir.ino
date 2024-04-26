int ledPin = 13;                // the pin that the LED is atteched to
int inputPin=2             // variable to store the sensor status (value)
int pirState=LOW;
int val=0;

void setup() {
  pinMode(ledPin, OUTPUT);      // initalize LED as an output
  pinMode(inputPin, INPUT);    // initialize sensor as an input
  Serial.begin(9600);        // initialize serial
}

void loop(){
  val = digitalRead(inputPin);   // read sensor value
  if (val == HIGH) {           // check if the sensor is HIGH
    digitalWrite(led, HIGH);   // turn LED ON
    if (pirState == LOW) {
      Serial.println("Motion detected!"); 
      pirState = HIGH;       // update variable state to HIGH
    }
  } 
  else {
      digitalWrite(ledPin, LOW); // turn LED OFF
      if (pirState == HIGH){
        Serial.println("Motion ended!");
        pirState = LOW;       // update variable state to LOW
    }
  }
}