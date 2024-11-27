# Microbit communication with a computer
Use a cloud broker and a wi-fi module to communicate using the IoT to a computer or other microbit.

This will be more like a **tutorial** than a **repository**, however this will contain code so I made a repo. 🙂

## Getting the Microbit online
In order to set up the Microbit we first need a couple of things:
- A Microbit
- An IoT bit
- Simple wifi (Username + Password only - although there are likley workarounds)
- Another computer with internet access (though seeing as you're reading this, you probably have one).

### You can see what to buy [__here__](Hardware/hardware.md)

- Flash the Microbit with the code in the src folder. (You will need to edit the Wi-fi settings first)
>See how to flash the Microbit, and other things alike, take a look at the [User Guide](https://microbit.org/get-started/user-guide/introduction/)
- And connect it to a power supply
- The screen should flash.
  
You also might want to tinker with my code; in that case there is also a Python & JS file with it.

## Getting a server (using a PC)
For this I used the free [Ably MQTT broker]((https://ably.com))
>Read the [docs](https://ably.com/docs)
- Create an account with ably (or I suppose another MQTT based broker)
- Create a new app
- Go to "API keys" and "Show"
- Copy the key to where the API is specified in src
>You should NEVER hard-code and API key, however for our purposes, we don't need to worry about security

- Run the code

Unfortunately, the code is only available in Python as I don't know JS or TS. However if anybody would be willing to translate into any other languages, that would be so much appreciated!!

## Getting a server (On the Microbit)
Again, copy the code accross and swap out the placeholders with your infomation, and flash.
