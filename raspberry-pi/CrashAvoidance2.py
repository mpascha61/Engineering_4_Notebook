#type: ignore 
import adafruit_mpu6050
import busio
import board
import time
import digitalio

sda_pin = (board.GP14)
scl_pin = (board.GP15)
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT
#i2c defines the 2 different i2c inputs
while True:
    print(mpu.acceleration)
    time.sleep(.1)
    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9 or mpu.acceleration[1] > 9  or mpu.acceleration[1] < -9: 
        led.value = True
    else:
        led.value = False
        time.sleep(.1)
    #while true is allowing the led to turn on while within the ranges given by inequalities