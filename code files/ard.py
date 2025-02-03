# sudo apt-get install python3-serial
# sudo chmod 666 /dev/ttyAM0


import serial
import time
import pyttsx3

arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=.1)

engine = pyttsx3.init()



file = open("file.txt", "r")
file2 = open("file2.txt", "r")
num = '0'
time.sleep(3)

while True:

    print("\nindex:", num)
    time.sleep(0.3)
    arduino.write(bytes(num, 'utf-8'))
    if (num == '9'):
        time.sleep(5)
        num='0'
    else:
        time.sleep(0.5)

    data_s = arduino.readline().decode('utf-8')
    data_s = data_s[:-2]
    data_t = arduino.readline().decode('utf-8')
    data_t = data_t[:-2]
    data_q = arduino.readline().decode('utf-8')
    data_q = data_q[:-2]


    if (data_t != '') and (data_s != '') and (data_q != ''):
        data_si = float(data_s)
        data_ti = float(data_t)
        data_qi = float(data_q)
        print("Distance:", data_si)
        print("SpO2:", data_qi)


        if (data_si > 7.0):
            print("Room Temperature:", data_ti)
            engine.say("Please place your hand on sensor.")
            engine.runAndWait()
            num = '0'
        else:
            print("Person Temperature:", data_ti)
            file.seek(0)
            seek = file.read(1)

            file2.seek(0)
            seek2 = file2.read(1)

            if (seek2 == '3'):
                print("Social Distance Violation")
                engine.say("Social Distance Violation")
                engine.runAndWait()
            elif (seek == '9' and data_ti < 38.0):
                if (data_qi <102 and data_qi> 79):
                    print("Opening door, please move along!")
                    engine.say("Yor temperature is" + str(data_ti))
                    engine.runAndWait()
                    engine.say("Opening door, please move along!")
                    engine.runAndWait()
                    num = '9'
                else:
                    print("SPO2 not adequate")
                    engine.say("S P O 2 not adequate")
                    engine.runAndWait()
                
                
            else:
                print ("You are not wearing facemask")
                engine.say("You are not wearing facemask")
                engine.runAndWait()

#file.close()
