ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("YOUR WIFI", "AND ITS PASSWORD")
basic.forever(function on_forever() {
    if (ESP8266_IoT.wifiState(true)) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.clearScreen()
        basic.pause(1000)
    }
    
})
