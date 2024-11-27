ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("YOUR WIFI", "AND ITS PASSWORD")
basic.forever(function () {
    if (!(ESP8266_IoT.isMqttBrokerConnected())) {
        ESP8266_IoT.setMQTT(
        ESP8266_IoT.SchemeList.TLS,
        "ANY THING, THIS WILL IDENTIFY THE MICROBIT",
        "UPTO THE ':' IN THE API KEY",
        "AFTER THE ':'",
        "mqtt"
        )
        ESP8266_IoT.connectMQTT("mqtt.ably.io", 8883, false)
        basic.pause(10000)
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
