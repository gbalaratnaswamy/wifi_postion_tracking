## ESP8266 code
for now I am using micropython for programming esp. In future I may also upload C/C++ code

first esp connects to one of the local wifi to wich our local server is running. then it scans for available networks and their signal strengths. then it takes multiple readings and average them and send their SSID BSSID and RSSI values to local server. then it goes to deep sleep to save power. after certain time RTC wakes it up so it again repeates its tasks