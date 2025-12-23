#include"DHT.h"
#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(115200);

  dht.begin

  Serial.println("DHT setup is done");
  // put your setup code here, to run once:

}

void loop() {
  float temp = dht.readTemperature();

  float humidity = dht.readHumidity();

  Serial.printf("Temperture = %f,Humidity = %f\n,temp,himudity");
  
  dealy(3000);
  // put your main code here, to run repeatedly:

}
