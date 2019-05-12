import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
import pigpio #importing GPIO library

ESC=4  #Connect the ESC in this GPIO pin 

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 #change this if your ESC's max value is different 
min_value = 700  #change this if your ESC's min value is different 
print "For first time launch, select calibrate"
print "Type the exact word for the function you want"
print "control OR stop"
                       
def control(): 
    print "Starting motor. If not calibrated and armed, restart by giving 'x'"
    time.sleep(1)
    speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
    print "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed"
    while True:
        pi.set_servo_pulsewidth(ESC, speed)
        inp = raw_input()
        if inp == "q":
            speed -= 100    # decrementing the speed 
            print "speed = %d" % speed
        elif inp == "e":    
            speed += 100    # incrementing the speed 
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10     # incrementing the speed 
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print "speed = %d" % speed
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "arm":
            arm()
            break	
        else:
            print "Press a,q,d or e"
            
        
def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

#This is the start of the program actually, to start the function it needs to be initialized before calling 
inp = raw_input()
if inp == "control":
    control()
elif inp == "stop":
    stop()
else :
    print "Restart program"

