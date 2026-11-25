import serial
import time




ser = serial.Serial('/dev/ttyUSB0', 19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 10 )
print(ser.name)

risposta = None
count = 0



while risposta != b'\n\r' and count < 3:
    command1 = '\n'
    ser.reset_input_buffer()
    ser.flush()
    ser.reset_output_buffer()
    time.sleep(0.5)
    command1 = command1.encode()
    ser.write(command1)
    time.sleep(2.6)
    risposta = ser.read_all()
    print(risposta)
    count += 1
    time.sleep(2.6)
    



print('consolle attiva')

count = 0
risposta = b''

while risposta == b'' and count < 3:
    command2 = 'LOOP 1\n'
    ser.reset_input_buffer()
    ser.flush()
    ser.reset_output_buffer()
    time.sleep(0.5)
    command2 = command2.encode()
    ser.write(command2)
    time.sleep(2.5)
    risposta = ser.read(100)
    print(risposta)
    count += 1

print('Inizio scrittura')

f = open('dati.txt', 'a')

for i in range (0, 10):
    ser.write(b'LOOP 1\n')
    time.sleep(2.6)
    risposta = ser.read(100)
    print(risposta)
    f.write(str(risposta))
    time.sleep(30)

f.close()


ser.close() 
