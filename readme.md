## WIFI Postion Tracking
The aim of this project is to locate object location (ESP 8266) without use of gps module. For locations in my collage (IITG) we have plenty of routers in collage, So We can use this to our advantage to locate using wifi AP and track object with low cost and at low power consumption within reasonable accuracy. If we keep this ESP module inside bicycle then we can track it with the help of RSSI value for nearby routers and by using mathemitacal calculations and original location of AP we can track the location of bicycle when lost.

The techinque we are using hear is Signal strength based which can be measuered by RSSI. We first measure signal strength from a ESP Module to several access points, and then combining this information with a propagation model to determine the distance between the client device and the access points. Trilateration techniques can be used to calculate the estimated client device position relative to the known position of access points.


# Cost Analysis
This device mainly consists of ESP8266 and battery (and some other minor components like usb connector for charging etc), ESP8266 module costs around ₹130/- and 300mah (LIPO) battery around ₹145/-. So each module costs within ₹300/-.


# Battery Life
we turn on ESP module every 10 min for scanning wifi signals and calculatins RSSI and sending data lo local server. This whole process completes within 700 ms and with average current of 140mA and during deepsleep current about 20uA(very small) attaining easily 60 days of battery life on paper.


## References
https://en.wikipedia.org/wiki/Wi-Fi_positioning_system
