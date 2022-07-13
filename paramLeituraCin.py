import serial

def checksum(array):
    sum = 0
    for i in array:
        sum = sum + i
    array.append(sum>>8)
    array.append(sum%256)
    return array


commandParamReadCin = [0xfa, 0xfb, 0xfc, 0xfd]
for i in range(57):
    commandParamReadCin.append(0x0)
commandParamReadCin[12] = 0x70
commandParamReadCin[15] = 0x09
commandParamReadCin[19] = 0x2B
commandParamReadCin[31] = 0x01

#num leituras - commandParamReadCin[23]
#tempo intervalo medidas - bytes 25, 26 e 27
#posição filtro - commandParamRead[35] 
#posição filtro (2 leitura) - commandParamRead[39]
#velocidade de leitura - commandParamRead[43]:
#commandParamRead[43] = 0x0 (fast) 
#commandParamRead[43] = 0x1 (standart)
#enable shake - commandParamRead[47]
#velocidade shake 1- commandParamRead[51]:
#commandParamRead[51] = 0x1 (low) 
#commandParamRead[51] = 0x2 (medium)
#commandParamRead[51] = 0x3 (high) 
#enable shake 0- commandParamRead[57]:
#commandParamRead[57] = 0x0 (first)
#commandParamRead[57] = 0x1 (every) 
#tempo de shake - bytes 53,54,55
#tempo de shake - bytes 58,59,60

commandParamReadCin[23] = 0x02 
commandParamReadCin[27] = 0x07
commandParamReadCin[35] = 0x01
commandParamReadCin[55] = 0x01
commandParamRead = checksum(commandParamReadCin)
commandParamReadCin = bytearray(commandParamReadCin) 
#print(commandParamReadCin)

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

ser.write(commandParamReadCin)
