import meshtastic
from pubsub import pub

def onReceive(packet): # called when a packet arrives
    print(f"Received: {packet}")

def onConnection(): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    interface.sendText("hello mesh")

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")
# By default will try to find a meshtastic device, otherwise provide a device path like /dev/ttyUSB0
interface = meshtastic.StreamInterface()


