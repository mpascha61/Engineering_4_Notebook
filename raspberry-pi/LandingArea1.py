#type: ignore

while True:
    print("Enter the first coordinate in format x,y:")
    Coordinate1 = input()
    print("Enter the second coordinate in format x,y:")
    Coordinate2 = input()
    print("Enter the third coordinate in format x,y:")
    Coordinate3 = input()

    Coordinate1 = Coordinate1.split(",")
    print(Coordinate1)

    #print(Coordinate1) <-- will print the (x,y)
    #print(Coordinate1[0]) <-- will print the first number (x), if i put [1] it will print the second number (y)

    Coordinate2 = Coordinate2.split(",")
    print(Coordinate2)
    Coordinate3 = Coordinate3.split(",")
    print(Coordinate3)
    x = float(3)
    try:
        print(x,y)
    except:
        print("An exception occurred")

  