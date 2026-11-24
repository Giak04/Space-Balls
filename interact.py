import serial
import time




ser = serial.Serial('/dev/ttyUSB0', 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 10 )
print(ser.name)

risposta = None
count = 0

while risposta != b'\n\r' and count < 3:
    command1 = '\n'
    command1 = command1.encode()
    ser.reset_input_buffer()
    time.sleep(0.5)
    ser.write(command1)
    time.sleep(1)
    risposta = ser.read_all()
    print(risposta)
    count += 1
    time.sleep(2.6)
    
    
print('consolle attiva')

count = 0
risposta = b''

while risposta == b'' and count < 3:
    command2 = 'LOOP 1'
    command2 = command2.encode()
    ser.reset_input_buffer()
    time.sleep(0.5)
    ser.write(command2)
    time.sleep(1)
    risposta = ser.read_all()
    print(risposta)
    count += 1
    time.sleep(10)

ser.close() 
