#type: ignore
import time 
import board
import digitalio

  led = digitalio.DigitalInOut(GP12.LED)
  led.direction = digitalio.Direction.OUTPUT

for counter in range(10, 0, -1):
  print(counter)
  time.sleep(1)

  
print("Liftoff!")
