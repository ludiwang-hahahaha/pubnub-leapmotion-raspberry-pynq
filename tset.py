from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import numpy as np

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pnconfig.uuid = "my_custom_uuid"
pubnub = PubNub(pnconfig)

boneDict = {}
fingerList = []
dirList0 = []
dirList1 = []
dirList2 = []

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
        msg1 = 0
        msg2 = 0
        msg3 = 0
        msg4 = 0
        msg0 = 0
        # list<dict<bone, list>>
        while message.channel == "finger":

           if  msg0 == 0:
                         fingerList.append(boneDict)
                         boneDict.clear()
                         msg0 =1
           break

        while message.channel == "bone":

            if msg1 == 0:
                        boneDict[message.message] = [dirList0, dirList1, dirList2]
                        msg1 = 1
            break

        while message.channel == "direction0":

           if msg2 == 0:
                           dirList0.append(message.message)
                           msg2 = 1
                           continue

        while message.channel == "direction1":

         if msg3 == 0:
                  dirList1.append(message.message)
                  msg3 =1
                  break

        while message.channel == "direction2":

           if msg4 == 0:
                    dirList2.append(message.message)
                    msg4 =1
                    break


        print fingerList
        print "dir0: %s" % dirList0
        print "dir1 :%s" % dirList1
        print "dir2 :%s" % dirList2

        while msg0 == 1 and msg1 == 1  and msg3 ==1 and msg4 == 1:
                      msg0 == 0
                      msg1 == 0
                      msg2 == 0
                      msg3 == 0
                      msg4 == 0

                      continue





    # Handle new message stored in message.message


pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('direction0').execute()
pubnub.subscribe().channels('direction1').execute()
pubnub.subscribe().channels('direction2').execute()
pubnub.subscribe().channels('finger').execute()
pubnub.subscribe().channels('bone').execute()