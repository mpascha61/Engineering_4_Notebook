#type: ignore
import time 
import digitalio 
import board 

led1 = digitalio.DigitalInOut(board.GP12)
led2 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
<<<<<<< HEAD
button = digitalio.DigialInOut(board.GP21)
=======
button = digitalio.DigitalInOut(board.GP21)
>>>>>>> d47822fd74568f7cf31676f608bba2dc61d72db5
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True:
<<<<<<< HEAD
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
=======
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
>>>>>>> d47822fd74568f7cf31676f608bba2dc61d72db5

while True: 
  passq
