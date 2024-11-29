def on_button_pressed_a():
    ESP8266_IoT.publish_mqtt_message("A", "Buttons", ESP8266_IoT.QosList.QOS0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_mqtt_qos_list_qos0(message):
    basic.show_string("" + (message))
ESP8266_IoT.mqtt_event("Buttons_Send",
    ESP8266_IoT.QosList.QOS0,
    on_mqtt_qos_list_qos0)

def on_button_pressed_b():
    ESP8266_IoT.publish_mqtt_message("B", "Buttons", ESP8266_IoT.QosList.QOS0)
input.on_button_pressed(Button.B, on_button_pressed_b)

ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("Wifi", "password)

def on_forever():
    if not (ESP8266_IoT.is_mqtt_broker_connected()):
        ESP8266_IoT.set_mqtt(ESP8266_IoT.SchemeList.TLS,
            "IDENTIFIER",
            "UPTO :",
            "AFTER :",
            "mqtt")
        ESP8266_IoT.connect_mqtt("mqtt.ably.io", 8883, False)
        basic.pause(10000)
basic.forever(on_forever)
