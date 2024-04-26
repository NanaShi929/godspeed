#include <Servo.h>
// Declare the Servo pin
int servoPin = 3;
// Create a servo object you can replace myservo with any other name
Servo myservo;
void setup() {
 // We need to attach the servo to the used pin number
 myservo.attach(servoPin);
}
void loop(){

 // Make servo go to 0 degrees
 myservo.write(0);
 delay(1000);

// Make servo go to 90 degrees
 myservo.write(90);
 delay(1000);

 // Make servo go to 180 degrees
 myservo.write(180);
 delay(1000);
}
