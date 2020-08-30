import meshtastic
import time
from pubsub import pub

#replynum = 0

def onReceive(packet): # called when a packet arrives
    print(f"Received: {packet}")
    if packet['decoded']['data'] is not None:
        msg = packet['decoded']['data']['text']
        rxSnr = packet['rxSnr']
        hopLimit = packet['hopLimit']
        print(f"message: {msg}")
        reply="got msg \'{}\' with rxSnr: {} and hopLimit: {}".format(msg,rxSnr,hopLimit)
        print("Sending reply: ",reply)
        interface.sendText(reply)
    #replynum=replynum+1

def onConnection(): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    interface.sendText("hello mesh")

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")
# By default will try to find a meshtastic device, otherwise provide a device path like /dev/ttyUSB0
interface = meshtastic.StreamInterface()


