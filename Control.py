from flask import Flask, render_template
from flask_socketio import SocketIO
# Import the PCA9685 module.
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


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

        print('Moving servos on channels 0-3, press Ctrl-C to quit...')
        
        # Move servo on channel O between extremes.
        #360=clockwise, 0=counterclockwise
        pwm.set_pwm(0, 0, servo_max) #Left Front Drive 
        pwm.set_pwm(1, 360, servo_max) #Right Front Drive
        pwm.set_pwm(2, 0, servo_max) #Left Rear Drive 
        pwm.set_pwm(3, 360, servo_max) #Right Rear Drive

    #Stop Forward Control      
    if message==5: 
        servo_min = 0  # Min pulse length out of 4096
        servo_max = 600  # Max pulse length out of 4096

      # Set frequency to 60hz, good for servos.
        pwm.set_pwm_freq(60)

        print('Moving servos on channels 0-3, press Ctrl-C to quit...')
        
        # Move servo on channel O between extremes.
        #360=clockwise, 0=counterclockwise
        pwm.set_pwm(0, 0, servo_min) #Left Front Drive 
        pwm.set_pwm(1, 0, servo_min) #Right Front Drive
        pwm.set_pwm(2, 0, servo_min) #Left Rear Drive 
        pwm.set_pwm(3, 0, servo_min) #Right Rear Drive

    #Reverse Control
    if message==3:
        servo_min = 150  # Min pulse length out of 4096
        servo_max = 600  # Max pulse length out of 4096


      # Set frequency to 60hz, good for servos.
        pwm.set_pwm_freq(60)

        print('Moving servo on channels 0-3, press Ctrl-C to quit...')
        
        # Move servo on channel O between extremes.
        #360=clockwise, 0=counterclockwise
        pwm.set_pwm(0, 360, servo_max) #Left Front Drive 
        pwm.set_pwm(1, 0, servo_max) #Right Front Drive
        pwm.set_pwm(2, 360, servo_max) #Left Rear Drive 
        pwm.set_pwm(3, 0, servo_max) #Right Rear Drive


    #Stop Reverse Control      
    if message==7: 
        servo_min = 0  # Min pulse length out of 4096
        servo_max = 600  # Max pulse length out of 4096

      # Set frequency to 60hz, good for servos.
        pwm.set_pwm_freq(60)

        print('Moving servos on channels 0-3, press Ctrl-C to quit...')
        
        # Move servo on channel O between extremes.
        #360=clockwise, 0=counterclockwise
        pwm.set_pwm(0, 0, servo_min) #Left Front Drive 
        pwm.set_pwm(1, 0, servo_min) #Right Front Drive
        pwm.set_pwm(2, 0, servo_min) #Left Rear Drive 
        pwm.set_pwm(3, 0, servo_min) #Right Rear Drive

    return render_template('index.html')
@app.route("/")
def root():
  message = "Hey World"
  return render_template('index.html',message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
    