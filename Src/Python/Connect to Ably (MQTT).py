ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("YOUR WIFI", "AND ITS PASSWORD")

def on_forever():
    if not (ESP8266_IoT.is_mqtt_broker_connected()):
        ESP8266_IoT.set_mqtt(ESP8266_IoT.SchemeList.TLS,
            "ANY THING, THIS WILL IDENTIFY THE MICROBIT",
            "UPTO THE : IN THE API KEY",
            "AFTER THE :",
            "mqtt")
        ESP8266_IoT.connect_mqtt("mqtt.ably.io", 8883, False)
        basic.pause(10000)
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)
