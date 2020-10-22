import sys
import datetime
import Leap
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time


t = time.time()
pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pnconfig.uuid = "my_custom_uuid"
pubnub = PubNub(pnconfig)

_frameId = -1
_frameTimeStamp = -1
_frameHands = -1
_frameFingers = -1


def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():

        pass  # Message successfully published to specified channel.
    else:

        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"
            #
            # print "  %s, id %d, position: %s" % (
            #     handType, hand.id, hand.palm_position)

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            # print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #     direction.pitch * Leap.RAD_TO_DEG,
            #     normal.roll * Leap.RAD_TO_DEG,
            #     direction.yaw * Leap.RAD_TO_DEG)

            # Get arm bone
            arm = hand.arm
            #print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
               # arm.direction,
                #arm.wrist_position,
                #arm.elbow_position)

            # Get fingers
            for finger in hand.fingers:

                #print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                    #self.finger_names[finger.type],
                    #finger.id,
                    #finger.length,
                    #finger.width)

                # Get bones
                for finger in hand.fingers:

                    #print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                       # self.finger_names[finger.type],
                       # finger.id,
                       # finger.length,
                       # finger.width)

                    if self.finger_names[finger.type] == "Middle":
                        # Get bones
                        for b in range(0, 4):
                            bone = finger.bone(b)
                            bbb = str(self.finger_names[finger.type]) + "," +str(self.bone_names[bone.type]) +str(bone.direction)
                            #
                            pubnub.publish().channel("direction0").message(bbb).pn_async(
                                    my_publish_callback)
                            print bbb
                               # bone.direction,
                            #)
                            #print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                            #for d in range(0, 3):






            if not frame.hands.is_empty:
                  print ""


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()