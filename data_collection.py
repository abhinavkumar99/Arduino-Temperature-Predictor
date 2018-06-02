import serial
from time import sleep
import csv
import datetime

with open('out.csv', 'w') as f:
   f.write('datetime,temp\n')
while True:
    f = open('out.csv', 'a', newline = '')
    writer = csv.writer(f)


    ser = serial.Serial('COM3', 9600)

    data = ser.readline()

    data = data.decode('utf-8')
    if len(data.split()) == 1 or len(data.split()) == 0:
        ser.close()
        continue

    out = data.strip()
    writer.writerow([datetime.datetime.now().isoformat(), out.split()[1]])
    print('written')
    f.close()
    #print(out)
    x = ser.close()
    sleep(.3)
