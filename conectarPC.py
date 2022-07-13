import serial

#Número de bytes para ler como resposta da conexão com o PC
NumBytesRead = 77

def checksum(array):
    sum = 0
    for i in array:
        sum = sum + i
    array.append(sum>>8)
    array.append(sum%256)
    return array

commandConnectPC = [0xfa, 0xfb, 0xfc, 0xfd]
for i in range(16):
    commandConnectPC.append(0x0)
commandConnectPC[12] = 0x70
commandConnectPC[19] = 0x02
commandConnectPC[14] = 0x00
commandConnectPC[15] = 0x01
commandConnectPC = checksum(commandConnectPC)
commandConnectPC = bytearray(commandConnectPC) 
#print(commandConnectPC)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

ser.write(commandConnectPC)
ser.flush()
ser.read(NumBytesRead)