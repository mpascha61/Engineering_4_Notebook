#type: ignore
import time 
import digitalio 
import board 

led1 = digitalio.DigitalInOut(board.GP12)
led2 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
#Both LEDS are defined with their given board positions

#counter counts backwards from 10 to 0
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
    #else statement says that any other value will trigger it
while True: 
  pass
