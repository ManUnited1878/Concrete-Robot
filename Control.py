from flask import Flask, render_template
from flask_socketio import SocketIO
# Import the PCA9685 module.
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()


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

    return render_template('index.html')
@app.route("/")
def root():
  message = "Hey World"
  return render_template('index.html',message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
    