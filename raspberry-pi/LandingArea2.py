#type: ignore
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import displayio
import busio
import board
displayio.release_displays()

def area_calc(x1, x2, x3, y1, y2, y3): #Find the coordinates
    area = abs((1/2) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    #area calculations defined
    return area

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
while True:
    print("Enter the first coordinate in format x,y:")
    Coordinate1 = input()
    print("Enter the second coordinate in format x,y:")
    Coordinate2 = input()
    print("Enter the third coordinate in format x,y:")
    Coordinate3 = input()
    splash = displayio.Group()
    display.show(splash)
    xaxis = Line(0,32,128,32, color=0xFFFF00)
    splash.append(xaxis)
    yaxis = Line(64,0,64,64, color=0xFFFF00)
    splash.append(yaxis)
    #drawing the x/y planes on the OLED
    try:
        Coordinate1 = Coordinate1.split(",")
        Coordinate2 = Coordinate2.split(",")
        Coordinate3 = Coordinate3.split(",")
    #print(Coordinate1) <-- will print the (x,y)
    #print(Coordinate1[0]) <-- will print the first number (x), if i put [1] it will print the second number (y)
        x1 = float(Coordinate1[0])
        x2 = float(Coordinate2[0])
        x3 = float(Coordinate3[0])
        
        y1 = float(Coordinate1[1])
        y2 = float(Coordinate2[1])
        y3 = float(Coordinate3[1])
        triangle = Triangle(int(x1) + 64 , (int(y1) + 32 ), (int(x2) + 64 ), (int(y2) + 32 ), (int(x3) + 64 ), (int(y3) + 32 ), outline=0xFFFF00)
        splash.append(triangle)
        area = area_calc(x1, x2, x3, y1, y2, y3)
        ans = area
        print(f"The area of the triangle with the vertices {Coordinate1}, {Coordinate2}, {Coordinate3} is {ans} kilometers squared")
    except:
        print("An exception occurred")       