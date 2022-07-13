import serial

def checksum(array):
    sum = 0
    for i in array:
        sum = sum + i
    array.append(sum>>8)
    array.append(sum%256)
    return array

commandParamRead = [0xfa, 0xfb, 0xfc, 0xfd]
for i in range(49):
    commandParamRead.append(0x0)
commandParamRead[12] = 0x70
commandParamRead[15] = 0x08
commandParamRead[19] = 0x23
commandParamRead[23] = 0x01

#posição filtro - commandParamRead[27] 
#posição filtro (2 leitura) - commandParamRead[31]
#velocidade de leitura - commandParamRead[35]:
#commandParamRead[35] = 0x0 (fast) 
#commandParamRead[35] = 0x1 (standart)
#enable shake - commandParamRead[40]
#velocidade shake 1- commandParamRead[43]:
#commandParamRead[43] = 0x1 (low) 
#commandParamRead[43] = 0x2 (medium)
#commandParamRead[43] = 0x3 (high) 
#tempo de shake - bytes 45,46,47
#tempo de shake - bytes 50,51,52

commandParamRead[27] = 0x01
commandParamRead[35] = 0x01
commandParamRead[47] = 0x01
commandParamRead = checksum(commandParamRead)
commandParamRead = bytearray(commandParamRead) 
#print(commandParamRead)

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

ser.write(commandParamRead)
