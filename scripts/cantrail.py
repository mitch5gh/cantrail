import os
#os.system('sudo ip link set can0 type can bitrate 100000')

import subprocess as sub

#p = sub.Popen(('sudo', 'tcpdump', '-l', '-i', 'can0'), stdout=sub.PIPE)        #to run realtime capture on rpi/can0
#p = sub.Popen(('sudo', 'tcpdump', '-l', '-i', 'enp5s0'), stdout=sub.PIPE)      #to run realtime capture on PC/NIC to test logic
p = sub.Popen(('sudo', 'tshark', '-r', 'wrx001.pcap'), stdout=sub.PIPE)         #for testing against playback of pcap file (so I don't have to do this in the garage)




for row in iter(p.stdout.readline, b''):
#    if "google" in row:                                                        # confirming logic works by going to google sites
#        print row.rstrip()                                                     # process here
    if "0x00000152" in row:                                                     #can address for turn signals
        print ("tsig loop ", row.rstrip())
        if "00 00 00 00 00 00 00 00" in row:                                    #can value for turn signal off
            print ("turn signal off ", row.rstrip())
        if "00 00 00 00 00 00 00 10" in row:                                    #can value for turn signal left 
            print ("turn signal left ", row.rstrip())
        if "00 00 00 00 00 00 00 20" in row:                                    #can value for turn signal right
            print ("turn signal right ", row.rstrip())
    if "0x00000OD1" in row:                                                     #can address for brake state
        print ("brake loop ", row.rstrip())
        if "00 00 00 00 00 00 00 00" in row:                                    #can value for brake pressure = 0
            print ("brake light off ", row.rstrip())
        if "00 00 00 00 00 00 00 00" not in row:                                #can value for brake pressure >0 0000 ##00 0000 0000
            print ("brake light on ", row.rstrip())
#    if "CAN" in row:                                                           #TS
#        print row.rstrip()
