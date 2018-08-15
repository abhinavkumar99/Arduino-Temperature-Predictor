import serial
from time import sleep
import csv
import datetime

with open('out.csv', 'w') as f:
   f.write('datetime,temp\n')

while True:
    f = open('out.csv', 'a', newline = '')
    writer = csv.writer(f)

    try:
        ser = serial.Serial('COM1', 9600)

        data = ser.readline()
    
    except PermissionError:
        f.close()
        ser.close()
        continue

    try:
        data = data.decode('utf-8')
    except UnicodeDecodeError:
        f.close()
        ser.close()
        continue
    
    if len(data.split()) == 1 or len(data.split()) == 0:
        f.close()
        ser.close()
        continue

    out = data.strip()
    writer.writerow([datetime.datetime.now().isoformat(), out.split()[1]])
    print('written')
    f.close()
    #print(out)
    x = ser.close()
    sleep(1)
