from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from numpy import *

import time
m=[]
r=[]
nowTime = lambda:int(round(t * 1000))
t = time.time()
pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pnconfig.uuid = "my_custom_uuid"
pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];


class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost

        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            pass
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.

    def message(self, pubnub, message):
        global m
        global r
        msg = str(message.message)
        print msg
        u0,u1=msg.split(":",1)
        u11,u12=u1.split(".",1)

        if "middle" in u0 and len(m)<1:
            m.append(u11)
        if "ring" in u0 and len (r)<1:
            r.append(u11)
        if len(m)==1 and len(r)==1:
            json_data = {

                'ring':   r[0],
                'middle': m[0],

            }
            print json_data
            pubnub.publish().channel("direction3").message(json_data).pn_async(my_publish_callback)
            m=[]
            r=[]

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('direction2').execute()
