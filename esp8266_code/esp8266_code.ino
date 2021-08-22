#include <ESP8266WiFi.h>

//SSID of your network
char ssid[] = "TP-Link_43D6";
//password of your WPA Network
char pass[] = "35401513";

void setup() {
  Serial.begin(115200);
  Serial.println("ESP8266 WiFi Signal Strength Checker");

  // Set WiFi to station mode and disconnect from an AP if it was previously connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(10);

  WiFi.begin(ssid, pass);
  Serial.print("Connecting...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // if you are connected, print out info about the connection:
  Serial.print("\nConnected to: ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("");
}

float prev = WiFi.RSSI(ssid);
float prev2= WiFi.RSSI("AndroidAP466E");
float alpha=0.5;
void loop () {
  // print the received signal strength:
  float rssi = WiFi.RSSI(ssid)*alpha+(1-alpha)*prev;
  float rssi2 = WiFi.RSSI("AndroidAP466E")*alpha+(1-alpha)*prev2;
  Serial.print("RSSI: ");
  Serial.println(rssi);
  Serial.print("RSSI2: ");
  Serial.println(rssi2);
  delay(300);
  prev=rssi;
  prev2=rssi2;
}
