#type: ignore
import time 
import digitalio 
import board 
import pwmio
from adafruit_motor import servo

led1 = digitalio.DigitalInOut(board.GP12)
led2 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

while True:
    if button.value == True:
  for counter in range(10, -1, -1):
  if counter is not 0:
    print(counter)
    led1.value = True
    time.sleep(.5)
    led1.value = False
    time.sleep(.5)

  else:
    print("Liftoff!")
    led2.value = True
    time.sleep(.5)
    led2.value = False 
    time.sleep(.5)
    servo1.angle = 180

while True: 
  pass
