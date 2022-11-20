import serial.tools.list_ports
import time

counter=0
ports = []
starT = 0.1
end_T = 0.1
comm1 = serial.Serial()

def Available():
    global starT
    global end_T
    global comm1
    starT = time.process_time()
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)
    print(ports)
    #print([port.device for port in serial.tools.list_ports.comports()])
    print ('listo:')
    if ports[0] == 'ttyACM0':
        comm1 = serial.Serial(port='/dev/ttyACM0',baudrate = 230400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
        print(type(comm1))
        print ("ok")
        #time.sleep(1)
        comm1.write("rgb,__red\n".encode('utf-8'))
        #time.sleep(4)
        end_T = time.process_time()#time.time_ns()
        print("Time taken", end_T-starT, "ns")
        return True
    
    else:
        print ("Nope")
        end_T = time.process_time()
        return False
    
def writeCMDser(cmnd):
    if Available():
        time.sleep(4)
        comm1.write(cmnd.encode('utf-8'))

#print(Available())
#print("Time taken", (end_T-starT) * 10**3, "ms")
#writeCMDser ()