import serial

#Número de bytes para ler como resposta da conexão com o PC
NumBytesRead = 26

def checksum(array):
    sum = 0
    for i in array:
        sum = sum + i
    array.append(sum>>8)
    array.append(sum%256)
    return array


commandInitRead = [0xfa, 0xfb, 0xfc, 0xfd]
for i in range(20):
    commandInitRead.append(0x0)
commandInitRead[12] = 0x70
commandInitRead[15] = 0x06
commandInitRead[19] = 0x06
commandInitRead[23] = 0x01

commandInitRead = checksum(commandInitRead)
commandInitRead = bytearray(commandInitRead) 
#print(commandInitRead)


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

ser.write(commandInitRead)
ser.flush()
x = ser.read(NumBytesRead)