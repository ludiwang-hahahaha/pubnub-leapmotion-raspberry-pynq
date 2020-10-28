from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import numpy as np
from numpy import *
import serial
import datetime
import time
from tkinter import *
t = time.time()
starttime = datetime.datetime.now()
pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'demo'
pnconfig.publish_key = 'demo'
pnconfig.uuid = "my_custom_uuid"
pubnub = PubNub(pnconfig)
json_data = {}
power_middle=[]
power_ring=[]
zuizhonga=[]
zuizhongi=[]
zuizhongj=[]
zuizhongk=[]
zuizhongl=[]
zuizhongb=[]
zuizhongc=[]
zuizhongd=[]
zuizhonge=[]
zuizhongf=[]
zuizhongg=[]
zuizhongh=[]
a={}
b={}
c={}
d={}
a_a={}
b_b={}
c_c={}
d_d={}
a_a_a={}
b_b_b={}
c_c_c={}
d_d_d={}
i=0
o=0
p=0
l=0
i_i=0
o_o=0
p_p=0
l_l=0
i_i_i=0
o_o_o=0
p_p_p=0
l_l_l=0

angle_f1 =0
angle_f2 =0
angle_f3 =0
angle_f4 =0
angle_f5 =0
angle_f6 =0

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
        allstarttime = datetime.datetime.now()
        pstarttime = datetime.datetime.now()
        msg = str(message.message)

        #print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'got')
        u0 ,u1 ,u2 ,u3,u4= msg.split(")" ,4)
        u00,u01=u0.split("(",1)
        u000,u001,u002 =u01.split(",",2)
        u00list=[float(u000),float(u001),float(u002)]
        u10,u11=u1.split("(",1)
        u100,u101,u102 =u11.split(",",2)
        u01list=[float(u100),float(u101),float(u102)]
        #print "u10: %s" % u10
        u20,u21=u2.split("(",1)
        u200,u201,u202 =u21.split(",",2)
        u02list=[float(u200),float(u201),float(u202)]
       # print "u20: %s" % u20
        u30,u31=u3.split("(",1)
        u300,u301,u302 =u31.split(",",2)
        u03list=[float(u300),float(u301),float(u302)]

        fingername = u4
        pendtime = datetime.datetime.now()
        print "ptime :" + str((pendtime - pstarttime).total_seconds())
        global a
        global b
        global c
        global d
        global a_a
        global b_b
        global c_c
        global d_d
        global a_a_a
        global b_b_b
        global c_c_c
        global d_d_d
        global i
        global o
        global p
        global l
        global i_i
        global o_o
        global p_p
        global l_l
        global i_i_i
        global o_o_o
        global p_p_p
        global l_l_l
        global zuizhongb
        global zuizhonga
        global zuizhongc
        global zuizhongd
        global zuizhongh
        global zuizhongf
        global zuizhongg
        global zuizhonge
        global zuizhongi
        global zuizhongj
        global zuizhongk
        global zuizhongl
        global angle_f1
        global angle_f2
        global angle_f3
        global angle_f4
        global angle_f5
        global angle_f6
        global json_data
        if "Middle" in fingername:
                #starttime = datetime.datetime.now()

                if i <= 4:
                    d.update({i: u00list})
                   # print ("d :"+str(d))
                    i = i + 1

                if o <= 4:
                    a.update({o: u03list})
                    o = o + 1
                    #print ("a :"+str(a))

                if p <= 4:
                    c.update({p: u01list})
                    p = p + 1
                    #print ("c:"+str(c))
                if l <= 4:
                    b.update({l: u02list})
                    l = l + 1
                   # print ("b:"+str (b))
                if i == 5:
                    dui1 = d[0]
                    dui2 = d[1]
                    dui3 = d[2]
                    dui4 = d[3]
                    dui5 = d[4]
                    i = 0
                    zuizhongd = []
                    d = {}
                    for w in range(0, 3):
                        xyz =[dui1[w],dui2[w],dui3[w],dui4[w],dui5[w]]
                        summm=np.median(xyz)
                        zuizhongd.append(summm)
                if p == 5:
                        dui1 = c[0]
                        dui2 = c[1]
                        dui3 = c[2]
                        zuizhongc = []
                        p = 0
                        c = {}
                        for w in range(0, 3):
                            summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                            zuizhongc.append(summm)
                if l == 5:
                        dui1 = b[0]
                        dui2 = b[1]
                        dui3 = b[2]
                        l = 0
                        zuizhongb = []
                        b = {}
                        for w in range(0, 3):
                            summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                            zuizhongb.append(summm)
                if o == 5:

                    dui1 = a[0]
                    dui2 = a[1]
                    dui3 = a[2]
                    o = 0
                    zuizhonga = []
                    a = {}
                    for w in range(0, 3):
                        summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                        zuizhonga.append(summm)

                      #  print zuizhonga
                       # print "aaaaaaaaaaaaa"
                if len(zuizhongd) == 3 and len(zuizhongb) == 3 and len(zuizhongc) == 3 and len(zuizhonga):
                    aaa = np.array(zuizhonga)
                    bbb = np.array(zuizhongb)
                    ccc = np.array(zuizhongc)
                    ddd = np.array(zuizhongd)
                    Lba = np.sqrt((aaa - bbb).dot(aaa - bbb))
                    Lbc = np.sqrt((ccc - bbb).dot(ccc - bbb))
                    Lcb = np.sqrt((bbb - ccc).dot(bbb - ccc))
                    Lcd = np.sqrt((ddd - ccc).dot(ddd - ccc))
                    # #
                    cos_angle1 = (bbb - ccc).dot(ddd - ccc) / (Lcb * Lcd)
                    angle_1 = np.arccos(cos_angle1)
                    angle_f1 = int(angle_1 * 360 / 2 / np.pi)

                    #print (angle_f1)


                    cos_angle2 = (aaa - bbb).dot(ccc - bbb) / (Lba * Lbc)
                    angle_2 = np.arccos(cos_angle2)
                    angle_f2 = int (angle_2 * 360 / 2 / np.pi)
                    #print angle_f2
                    #print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'middle')
                    zuizhongc = []
                    zuizhonga = []
                    zuizhongb = []
                    zuizhongd = []
                    #endtime = datetime.datetime.now()

                    #print "middletime :"+str((endtime - starttime).total_seconds())
        if "Ring" in fingername:
                if i_i <= 2:
                    d_d.update({i_i: u00list})
                    i_i = i_i + 1

                if o_o <= 2:
                    a_a.update({o_o: u03list})
                    o_o = o_o + 1

                if p_p <= 2:
                    c_c.update({p_p: u01list})
                    p_p = p_p + 1
                    # print c
                if l_l <= 2:
                    b_b.update({l_l: u02list})
                    l_l = l_l + 1
                # print b
                if i_i == 3:
                    dui1 = d_d[0]
                    dui2 = d_d[1]
                    dui3 = d_d[2]
                    i_i = 0
                    zuizhongf = []
                    d_d = {}
                    for w in range(0, 3):
                        summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                        zuizhongf.append(summm)
                if p_p == 3:
                        dui1 = c_c[0]
                        dui2 = c_c[1]
                        dui3 = c_c[2]
                        zuizhongg = []
                        p_p = 0
                        c_c = {}
                        for w in range(0, 3):
                            summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                            zuizhongg.append(summm)
                if l_l == 3:
                        dui1 = b_b[0]
                        dui2 = b_b[1]
                        dui3 = b_b[2]
                        l_l = 0
                        zuizhongh = []
                        b_b = {}
                        for w in range(0, 3):
                            summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                            zuizhongh.append(summm)
                if o_o == 3:
                    dui1 = a_a[0]
                    dui2 = a_a[1]
                    dui3 = a_a[2]
                    o_o = 0
                    zuizhonge = []
                    a_a = {}
                    for w in range(0, 3):
                        summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                        zuizhonge.append(summm)


                if len(zuizhongf) == 3 and len(zuizhongh) == 3 and len(zuizhongg) == 3 and len(zuizhonge)==3:
                    aaa = np.array(zuizhonge)
                    bbb = np.array(zuizhongf)
                    ccc = np.array(zuizhongg)
                    ddd = np.array(zuizhongh)
                    Lba = np.sqrt((aaa - bbb).dot(aaa - bbb))
                    Lbc = np.sqrt((ccc - bbb).dot(ccc - bbb))
                    Lcb = np.sqrt((bbb - ccc).dot(bbb - ccc))
                    Lcd = np.sqrt((ddd - ccc).dot(ddd - ccc))
                    # #
                    cos_angle1 = (bbb - ccc).dot(ddd - ccc) / (Lcb * Lcd)
                    angle_1 = np.arccos(cos_angle1)
                    angle_f3 = int(angle_1 * 360 / 2 / np.pi)
                    #print angle_f3
                    power_ring.append(angle_f2)

                    cos_angle2 = (aaa - bbb).dot(ccc - bbb) / (Lba * Lbc)
                    angle_2 = np.arccos(cos_angle2)
                    angle_f4 =int (angle_2 * 360 / 2 / np.pi)
                    #print angle_f4
                    #print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'ring')
                    zuizhonge = []
                    zuizhongf = []
                    zuizhongg = []
                    zuizhongh = []
        if "Pinky" in fingername:
                if i_i_i <= 2:
                    d_d_d.update({i_i_i: u00list})
                    i_i_i = i_i_i + 1

                if o_o_o <= 2:
                    a_a_a.update({o_o_o: u03list})
                    o_o_o = o_o_o + 1

                if p_p_p <= 2:
                    c_c_c.update({p_p_p: u01list})
                    p_p_p = p_p_p + 1
                    # print c
                if l_l_l <= 2:
                    b_b_b.update({l_l_l: u02list})
                    l_l_l = l_l_l + 1
                # print b
                if i_i_i == 3:
                    dui1 = d_d_d[0]
                    dui2 = d_d_d[1]
                    dui3 = d_d_d[2]
                    i_i_i = 0
                    zuizhongi = []
                    d_d_d = {}
                    for w in range(0, 3):
                        summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                        zuizhongi.append(summm)
                if p_p_p == 3:
                        dui1 = c_c_c[0]
                        dui2 = c_c_c[1]
                        dui3 = c_c_c[2]
                        zuizhongl = []
                        p_p_p = 0
                        c_c_c = {}
                        for w in range(0, 3):
                            summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                            zuizhongl.append(summm)
                if l_l_l == 3:
                        dui1 = b_b_b[0]
                        dui2 = b_b_b[1]
                        dui3 = b_b_b[2]
                        l_l_l = 0
                        zuizhongj = []
                        b_b_b = {}
                        for w in range(0, 3):
                            summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                            zuizhongj.append(summm)
                if o_o_o == 3:
                    dui1 = a_a_a[0]
                    dui2 = a_a_a[1]
                    dui3 = a_a_a[2]
                    o_o_o = 0
                    zuizhongk = []
                    a_a_a = {}
                    for w in range(0, 3):
                        summm = (dui1[w] + dui2[w] + dui3[w]) / 3
                        zuizhongk.append(summm)


                if len(zuizhongi) == 3 and len(zuizhongj) == 3 and len(zuizhongl) == 3 and len(zuizhongk)==3:
                    aaa = np.array(zuizhongi)

                    bbb = np.array(zuizhongj)

                    ccc = np.array(zuizhongk)
                    ddd = np.array(zuizhongl)
                    Lba = np.sqrt((aaa - bbb).dot(aaa - bbb))
                    Lbc = np.sqrt((ccc - bbb).dot(ccc - bbb))
                    Lcb = np.sqrt((bbb - ccc).dot(bbb - ccc))
                    Lcd = np.sqrt((ddd - ccc).dot(ddd - ccc))

                    cos_angle1 = (bbb - ccc).dot(ddd - ccc) / (Lcb * Lcd)
                    angle_1 = np.arccos(cos_angle1)
                    angle_f5 = int(angle_1 * 360 / 2 / np.pi)
                    #print angle_f3
                   # power_ring.append(angle_f2)

                    cos_angle2 = (aaa - bbb).dot(ccc - bbb) / (Lba * Lbc)
                    angle_2 = np.arccos(cos_angle2)
                    angle_f6 =int (angle_2 * 360 / 2 / np.pi)
                    #print angle_f4
                    #print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'ring')
                    zuizhongi = []
                    zuizhongl = []
                    zuizhongj = []
                    zuizhongk = []

        json_data = {

            'middle_bcd': angle_f2,
            'middle_abc': angle_f1,
            "ring_abc" : angle_f3,
            "ring_bcd" : angle_f4,
            "pinky_abc": angle_f5,
            "pinky_bcd":angle_f6,

        }
        # if angle_f1 >0 and angle_f2 >0 and angle_f3 >0 and angle_f4 >0 and angle_f5 >0 and angle_f6 >0:
        #        endtime = datetime.datetime.now()
        #        print "alltime :" + str((endtime - starttime).total_seconds())
        print json_data

        pubnub.publish().channel("abc").message(json_data).pn_async(my_publish_callback)
    pass

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('direction0').execute()
pubnub.subscribe().channels('direction1').execute()