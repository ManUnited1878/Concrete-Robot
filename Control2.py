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

pwm = Adafruit_PCA9685.PCA9685()

#ESC Variables
ESC=4  #Connect the ESC in this GPIO pin 

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 2000 #change this if your ESC's max value is different 
min_value = 700  #change this if your ESC's min value is different 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initial Steering Servo Settings
servo_Home = 400  # Min pulse length out of 4096
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
pwm.set_pwm(4, 0, servo_Home) #Left Servo
pwm.set_pwm(5, 0, servo_Home) #Right Servo


#@socketio.on('myevent')
#def handle_message(message):
#    print('received message: ' + message)


@socketio.on('arrows')
def handle_message(message):
    print('received message: ' + str(message))
    
    #Forward Control
    while message==8:
        print('Slow')
        if message==1:
            servo_min = 150  # Min pulse length out of 4096
            servo_max = 200  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)

            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(0, 0, servo_max) #Left Front Drive 
            pwm.set_pwm(1, 360, servo_max) #Right Front Drive
            pwm.set_pwm(2, 0, servo_max) #Left Rear Drive 
            pwm.set_pwm(3, 360, servo_max) #Right Rear Drive

            print('Forward')

        #Reverse Control
        if message==3:
            servo_min = 150  # Min pulse length out of 4096
            servo_max = 600  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(0, 360, servo_max) #Left Front Drive 
            pwm.set_pwm(1, 0, servo_max) #Right Front Drive
            pwm.set_pwm(2, 360, servo_max) #Left Rear Drive 
            pwm.set_pwm(3, 0, servo_max) #Right Rear Drive

            print('Reverse')

        #Left Steering
        if message==0:
            servo_Dir1 = 375  # Min pulse length out of 4096
            servo_Dir2 = 525  # Max pulse length out of 4096
        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(4, 0, servo_Dir1) #Left Servo
            pwm.set_pwm(5, 0, servo_Dir2) #Right Servo
        
            print('Left Steering')

        #Right Steering
        if message==0:
            servo_Dir1 = 375  # Min pulse length out of 4096
            servo_Dir2 = 525  # Max pulse length out of 4096
        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(4, 0, servo_Dir2) #Left Servo
            pwm.set_pwm(5, 0, servo_Dir1) #Right Servo
        
            print('Right Steering')


        #Stop Forward,Reverse, or Steering movement       
        if message==4 or message==5 or message==6 or message==7: 
            servo_min = 0  # Min pulse length out of 4096
            servo_Home = 400  # Min pulse length out of 4096

        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            # Stop Drive Servos
            pwm.set_pwm(0, 0, servo_min) #Left Front Drive 
            pwm.set_pwm(1, 0, servo_min) #Right Front Drive
            pwm.set_pwm(2, 0, servo_min) #Left Rear Drive 
            pwm.set_pwm(3, 0, servo_min) #Right Rear Drive
            #Return Steering Servos to original position
            pwm.set_pwm(4, 0, servo_Home) #Left Servo
            pwm.set_pwm(5, 0, servo_Home) #Right Servo


    while message==9:
        print('Fast')
        if message==1:
            servo_min = 150  # Min pulse length out of 4096
            servo_max = 600  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)

            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(0, 0, servo_max) #Left Front Drive 
            pwm.set_pwm(1, 360, servo_max) #Right Front Drive
            pwm.set_pwm(2, 0, servo_max) #Left Rear Drive 
            pwm.set_pwm(3, 360, servo_max) #Right Rear Drive

            print('Forward')

        #Reverse Control
        if message==3:
            servo_min = 150  # Min pulse length out of 4096
            servo_max = 600  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(0, 360, servo_max) #Left Front Drive 
            pwm.set_pwm(1, 0, servo_max) #Right Front Drive
            pwm.set_pwm(2, 360, servo_max) #Left Rear Drive 
            pwm.set_pwm(3, 0, servo_max) #Right Rear Drive

            print('Reverse')

        #Left Steering
        if message==0:
            servo_Dir1 = 375  # Min pulse length out of 4096
            servo_Dir2 = 525  # Max pulse length out of 4096
        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(4, 0, servo_Dir1) #Left Servo
            pwm.set_pwm(5, 0, servo_Dir2) #Right Servo
        
            print('Left Steering')

        #Right Steering
        if message==0:
            servo_Dir1 = 375  # Min pulse length out of 4096
            servo_Dir2 = 525  # Max pulse length out of 4096
        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            #360=clockwise, 0=counterclockwise
            pwm.set_pwm(4, 0, servo_Dir2) #Left Servo
            pwm.set_pwm(5, 0, servo_Dir1) #Right Servo
        
            print('Right Steering')


        #Stop Forward,Reverse, or Steering movement       
        if message==4 or message==5 or message==6 or message==7: 
            servo_min = 0  # Min pulse length out of 4096
            servo_Home = 400  # Min pulse length out of 4096

        # Set frequency to 60hz, good for servos.
            pwm.set_pwm_freq(60)
            
            # Stop Drive Servos
            pwm.set_pwm(0, 0, servo_min) #Left Front Drive 
            pwm.set_pwm(1, 0, servo_min) #Right Front Drive
            pwm.set_pwm(2, 0, servo_min) #Left Rear Drive 
            pwm.set_pwm(3, 0, servo_min) #Right Rear Drive
            #Return Steering Servos to original position
            pwm.set_pwm(4, 0, servo_Home) #Left Servo
            pwm.set_pwm(5, 0, servo_Home) #Right Servo


    #Turn Propellers On 
    if message==10:
        print('ESC ON')
        print ("control OR stop")
                       
        def control(): 
            print ("Starting motor. If not calibrated and armed, restart by giving 'x'")
            time.sleep(1)
            speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
            print ("Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed")
            while True:
                pi.set_servo_pulsewidth(ESC, speed)
                inp = raw_input()
                if inp == "q":
                    speed -= 100    # decrementing the speed 
                    print ("speed = %d" % speed)
                elif inp == "e":    
                    speed += 100    # incrementing the speed 
                    print ("speed = %d" % speed)
                elif inp == "d":
                    speed += 10     # incrementing the speed 
                    print ("speed = %d" % speed)
                elif inp == "a":
                    speed -= 10     # decrementing the speed
                    print ("speed = %d" % speed)
                elif inp == "stop":
                    stop()          #going for the stop function
                    break
                elif inp == "arm":
                    arm()
                    break	
                else:
                    print ("Press a,q,d or e")
                    
                
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
            print ("Restart program")

      
@socketio.on('ESC')
def handle_message(message):
    print('received message: ' + str(message))
    
    return render_template('index.html')
@app.route("/")
def root():
  message = "Hey World"
  return render_template('index.html',message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
    