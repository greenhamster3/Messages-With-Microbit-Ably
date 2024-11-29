input.onButtonPressed(Button.A, function () {
    ESP8266_IoT.publishMqttMessage("A", "Buttons", ESP8266_IoT.QosList.Qos0)
})
ESP8266_IoT.MqttEvent("Buttons_Send", ESP8266_IoT.QosList.Qos0, function (message) {
    basic.showString("" + (message))
})
input.onButtonPressed(Button.B, function () {
    ESP8266_IoT.publishMqttMessage("B", "Buttons", ESP8266_IoT.QosList.Qos0)
})
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("WIFI", "PASSWORD)
basic.forever(function () {
    if (!(ESP8266_IoT.isMqttBrokerConnected())) {
        ESP8266_IoT.setMQTT(
        ESP8266_IoT.SchemeList.TLS,
        "Micro",
        "UPTO :  IN THE API KEY",
        "AFTER :",
        "mqtt"
        )
        ESP8266_IoT.connectMQTT("mqtt.ably.io", 8883, false)
        basic.pause(10000)
    }
})
