#include <DHT.h>
#include <TM1637Display.h>
#define DHTPIN 3 // Replace with the digital pin connected to the DHT sensor
#define DHTTYPE DHT11 // Use DHT11 or DHT22 based on your sensor
#define CLK 4
#define DIO 5
DHT dht(DHTPIN, DHTTYPE);
TM1637Display display(CLK, DIO); // CLK to D3, DIO to D4
void setup() {
 Serial.begin(9600);
 dht.begin();
 display.setBrightness(0x0e); // Adjust brightness (0x00 to 0x0f)
}
void loop() {
 float humidity = dht.readHumidity();
 float temperature = dht.readTemperature();
 Serial.print("Temperature Celcius: ");
 Serial.print(temperature);
 if(temperature<=31){
  Serial.print("dead");
 }
 Serial.print(" °C | Humidity: ");
 Serial.print(humidity);
 Serial.println(" %");
 if (isnan(humidity) || isnan(temperature)) {
 display.showNumberDec(8888); // Display "8888" if there's an error
 } else {
 // Display temperature and humidity on the TM1637 module
 int tempInt = static_cast<int>(temperature);
 int humInt = static_cast<int>(humidity);
 int combined = tempInt * 100 + humInt;
 display.showNumberDec(combined);
 }
 delay(2000); // Update every 2 seconds
}
