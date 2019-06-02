import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
import pigpio #importing GPIO library

ESC=4  #Connect the ESC in this GPIO pin 

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 #change this if your ESC's max value is different 
min_value = 700  #change this if your ESC's min value is different 

print "Connect the battery and press Enter"
inp = raw_input()    
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
        pi.set_servo_pulsewidth(ESC, 0)         #going for the stop function
        break
