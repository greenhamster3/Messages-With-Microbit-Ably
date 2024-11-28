#there isn't a js, if you're reading this and could translate, I'd be very grateful
import asyncio #pip install asyncio
from ably import AblyRealtime #pip install ably
import base64
async def main():

    ably = AblyRealtime('entire key') #create the client object
    await ably.connection.once_async('connected') #connect

    buttons = ably.channels.get('Buttons') #get the chanels
    buttonsSend = ably.channels.get('Buttons_Send')

    async def listener(message): #on message
        message = message.as_dict() #get the message in a readable form, in this case a hash map
        decodedMessage = base64.b64decode(message["data"]).decode('utf-8') #decode from B64 to UTF-8
        print(decodedMessage)
        if decodedMessage == "A":
            await buttonsSend.publish("", "The a was pressed")
        elif decodedMessage == "B":
            await buttonsSend.publish("", "Hi")
    await buttons.subscribe(listener) #wait until a message on buttons arrives, then run the listner func
    await asyncio.Event().wait() #wait forever

asyncio.run(main()) #must be run asyncronously so it can wait to connect before connecting to send a message
