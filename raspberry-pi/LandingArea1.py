#type: ignore

def area_calc(x1, x2, x3, y1, y2, y3): #Find the coordinates
    area = abs((1/2) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    #equation for area defined above
    return area
while True:
    print("Enter the first coordinate in format x,y:")
    Coordinate1 = input()
    print("Enter the second coordinate in format x,y:")
    Coordinate2 = input()
    print("Enter the third coordinate in format x,y:")
    Coordinate3 = input()
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
        area = area_calc(x1, x2, x3, y1, y2, y3)
        ans = area
        print(f"The area of the triangle with the vertices {Coordinate1}, {Coordinate2}, {Coordinate3} is {ans} kilometers squared")
    except:
        print("An exception occurred")