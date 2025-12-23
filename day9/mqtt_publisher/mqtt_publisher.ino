#include<WiFi.h>
#include<ArduinoMqttClient.h>
#include<DHT.h>

const char *ssid = "Darshana";
const char *password = "87654321";

const char *host = "172.18.4.146";
unsigned int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE  DHT11

DHT dht(DHT_PIN, DHT_TYPE);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  dht.begin();g

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi ");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
    float hum  = dht.readHumidity();   


  WiFiClient wifiClient;
  MqttClient publisher(wifiClient);

  if(publisher.connect(host, port)){
    publisher.beginMessage("reading/temp");
    publisher.print(temp);
    publisher.endMessage();
    
    publisher.beginMessage("reading/humidity");
    publisher.print(hum);
    publisher.endMessage();


  }

  delay(5000);

}

