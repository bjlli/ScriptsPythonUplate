import serial

def checksum(array):
    sum = 0
    for i in array:
        sum = sum + i
    array.append(sum>>8)
    array.append(sum%256)
    return array

commandDisconnectPC = [0xfa, 0xfb, 0xfc, 0xfd]
for i in range(16):
    commandDisconnectPC.append(0x0)
commandDisconnectPC[12] = 0x70
commandDisconnectPC[19] = 0x02
commandDisconnectPC[14] = 0x00
commandDisconnectPC[15] = 0x02
commandDisconnectPC = checksum(commandDisconnectPC)
commandDisconnectPC = bytearray(commandDisconnectPC) 
#print(commandDisconnectPC)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

ser.write(commandDisconnectPC)