#type: ignore 
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio 
import displayio
import board
import time
import busio
import digitalio
import adafruit_mpu6050
displayio.release_displays() #put this line just below your imports
 


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(mpu.acceleration)
    time.sleep(.1)
    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9 or mpu.acceleration[1] > 9  or mpu.acceleration[1] < -9: 
        led.value = True
    else:
        led.value = False
        time.sleep(.1)

# create the display group
    splash = displayio.Group()

# add title block to display group
    title = "ANGULAR VELOCITY"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)  
  
    title = f"X {round(mpu.gyro[0],3)} rad/s"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=20)
    splash.append(text_area) 
    title = f"Y {round(mpu.gyro[1],3)} rad/s"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=35)
    splash.append(text_area) 
    title = f"Z {round(mpu.gyro[2],3)} rad/s"
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=50)
    splash.append(text_area) 





# the order of this command is (font, text, text color, and location)
# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don't forget to round the angular velocity values to three decimal places

# send display group to screen
    display.show(splash)