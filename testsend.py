import time
import meshtastic
interface = meshtastic.StreamInterface()

packetnum = 2
sleeptime = 10

while True:
    msg="hello {}".format(packetnum)    
    print("Sending",msg)
    interface.sendText(msg)
    packetnum = packetnum + 1
    time.sleep(sleeptime)
