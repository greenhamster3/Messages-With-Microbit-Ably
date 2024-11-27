ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("YOUR WIFI", "AND ITS PASSWORD")

def on_forever():
    if ESP8266_IoT.wifi_state(True):
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.clear_screen()
        basic.pause(1000)
basic.forever(on_forever)
