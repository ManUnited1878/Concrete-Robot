from flask import Flask, render_template
from flask_socketio import SocketIO
# Import the PCA9685 module.
import Adafruit_PCA9685
#Imports for ESC
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import picamera #Import camera module

pwm = Adafruit_PCA9685.PCA9685()

#ESC Variables
ESC1=4  #Connect the Propeller ESC in this GPIO pin 
ESC2=18  #Connect the DC Motor ESC in this GPIO pin 
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC1, 0) 
pi.set_servo_pulsewidth(ESC2, 0)
max_value = 2000 #change this if your ESC's max value is different 
min_value = 700  #change this if your ESC's min value is different 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initial Servo Settings
servo_min = 0  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_Home = 350  # Min pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#Neutral Steering Servo Settings
pwm.set_pwm(4, 0, servo_Home) #Left Servo
pwm.set_pwm(5, 0, servo_Home) #Right Servo


#@socketio.on('myevent')
#def handle_message(message):
#    print('received message: ' + message)


@socketio.on('arrows')
def handle_message(message):
    print('received message: ' + str(message))

    #Forward Control
    if message==1:
        speed = 1700 
        pi.set_servo_pulsewidth(ESC2, speed)
        print('Forward')
    elif message==5:         # Stop Drive Servos
        speed = 0
        pi.set_servo_pulsewidth(ESC2, speed)
  
    #Reverse Control
    if message==3:
        speed = 1300 
        pi.set_servo_pulsewidth(ESC2, speed)
        print('Reverse')
    elif message==7:        # Stop Drive Servos
        speed = 0
        pi.set_servo_pulsewidth(ESC2, speed)
 
    #Left Steering
    if message==0:
        servo_Dir1 = 250  # Min pulse length out of 4096
        servo_Dir2 = 450  # Max pulse length out of 4096
        pwm.set_pwm(4, 0, servo_Dir1) #Right Servo
        print('Left Steering')
 
    #Right Steering
    if message==2:
        servo_Dir1 = 250  # Min pulse length out of 4096 375
        servo_Dir2 = 450  # Max pulse length out of 4096 525
        pwm.set_pwm(4, 0, servo_Dir2) #Right Servo  
        print('Right Steering')
 
    #Stop Steering Movement       
    elif message==4 or message==6:      
        #Return Steering Servos to original position
        pwm.set_pwm(4, 0, servo_Home) #Left Servo
 
    #Camera - Still Photo Capture
    if message==10:
        print('Camera')
        camera = picamera.PiCamera()
        camera.capture('example.jpg')
        camera.vflip = True
        camera.capture('example2.jpg')

    #ESC Activation    
    if message==11:
        print('ESC ON')
        print "control OR stop"
                       
        def control(): 
            print "Starting motor. If not calibrated and armed, restart by giving 'x'"
            time.sleep(1)
            speed = 700  #1500  # change your speed if you want to.... it should be between 700 - 2000
            print "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed"
            while True:
                pi.set_servo_pulsewidth(ESC1, speed)
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
            pi.set_servo_pulsewidth(ESC1, 0)
            pi.stop()

   #ESC Speed Control
    if message==10:
        speed += 100
    if message==12:
        speed -= 100

        #This is the start of the program actually, to start the function it needs to be initialized before calling 
        inp = raw_input()
        if inp == "control":
            control()
        elif inp == "stop":
            stop()
        else :
            print "Restart program"

    #Emergency Off Switch
    if message==8:
        pi.set_servo_pulsewidth(ESC1, 0) #Turn off Propellers
        pi.set_servo_pulsewidth(ESC2, 0) #Turn off DC motors


    return render_template('index.html')
@app.route("/")
def root():
  message = "Hey World"
  return render_template('index.html',message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
    