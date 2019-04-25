# Simple demo of of the PCA9685 PWM servo/LED controller library.
from __future__ import division
from flask import Flask, render_template, request
import time
# Import the PCA9685 module.
import Adafruit_PCA9685

app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
  message = "Hey World"
  return render_template('index.html',message=message)

@app.route("/servos",methods=['GET','POST'])
def servos():
  clicked=None
  if request.method == "POST":
    # Uncomment to enable debug output.
    #import logging
    #logging.basicConfig(level=logging.DEBUG)

    # Initialise the PCA9685 using the default address (0x40).
      pwm = Adafruit_PCA9685.PCA9685()

    # Alternatively specify a different address and/or bus:
    #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

    # Configure min and max servo pulse lengths
      servo_min = 150  # Min pulse length out of 4096
      servo_max = 600  # Max pulse length out of 4096


    # Set frequency to 60hz, good for servos.
      pwm.set_pwm_freq(60)

      print('Moving servo on channels 0-3, press Ctrl-C to quit...')
      while True:
        # Move servo on channel O between extremes.
        #360=clockwise, 0=counterclockwise
        pwm.set_pwm(0, 0, servo_max) #Left Front Drive 
        time.sleep(1)
        pwm.set_pwm(1, 360, servo_max) #Right Front Drive
        time.sleep(1)
        pwm.set_pwm(2, 0, servo_max) #Left Rear Drive 
        time.sleep(1)
        pwm.set_pwm(3, 360, servo_max) #Right Rear Drive
        time.sleep(1)
  return render_template('index.html')



@app.route("/stop",methods=['GET','POST'])
def servos():
  clicked=None
  if request.method == "POST":
    # Uncomment to enable debug output.
    #import logging
    #logging.basicConfig(level=logging.DEBUG)

    # Initialise the PCA9685 using the default address (0x40).
      pwm = Adafruit_PCA9685.PCA9685()

    # Alternatively specify a different address and/or bus:
    #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

    # Configure min and max servo pulse lengths
      servo_min = 0  # Min pulse length out of 4096
      servo_max = 600  # Max pulse length out of 4096


    # Set frequency to 60hz, good for servos.
      pwm.set_pwm_freq(60)

      print('Stop servos on channels 0-3, press Ctrl-C to quit...')
      while True:
        # Move servo on channel O between extremes.
        #360=clockwise, 0=counterclockwise
        pwm.set_pwm(0, 0, servo_min) #Left Front Drive 
        time.sleep(1)
        pwm.set_pwm(1, 360, servo_min) #Right Front Drive
        time.sleep(1)
        pwm.set_pwm(2, 0, servo_min) #Left Rear Drive 
        time.sleep(1)
        pwm.set_pwm(3, 360, servo_min) #Right Rear Drive
        time.sleep(1)
  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')


