import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print("Waiting for sensor to settle")

      time.sleep(2)

      print("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print "Distance:",distance,"cm"

finally:
      GPIO.cleanup()

#Activate Bending Servo
if distance<=4:
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096

    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

    #360=clockwise, 0=counterclockwise
    pwm.set_pwm(0, 0, servo_max) #Chassis Bending Servo 