from __future__ import division
import time

# import curses (key input software)
import curses
# Import the PCA9685 module
import Adafruit_Python_PCA9685


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_Python_PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


try:
  while True:
    char = screen.getch()

    if char == curses.KEY_UP:
      print ('up')
      # Move servo on channel O between extremes.
      # pwm.set_pwm(servo pin (0-16), PWM, servo_max)
      pwm.set_pwm(0, 360, servo_max)#360=clockwise, 0=counterclockwise
      time.sleep(1)
      pwm.set_pwm(1, 0, servo_max)
      time.sleep(1)

    print('Moving servo on channel 0 and 1, press Ctrl-C to quit...')
    
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
