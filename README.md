# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Launch_Pad

### Assignment Description
Launch Pad Part 1:
Countdown from 10 to 0 and then saying liftoff, simulating a launch of a rocket here.

### Evidence 

![Countdown](images/countdown.gif)

### Wiring

No wiring was necessary for this part

### Code
[Code for the countdown](raspberry-pi/LaunchPad1.py)

### Reflection

To start out I tried using a counter without knowing how the values of interments worked. I had to do some research using the links embedded in the document of the assignment and help from a classmate on some syntax issues such as not adding a colon at the end of a for loop, not making my interment # negative, and forgetting parenthesees. 

### Assignment Description

Launch Pad Part 2: The second part to the launch pad combines the use of the countdown from part one and elements of the LED blink assignment. Every second of a the countdown the red led goes off, and upon liftoff the green goes off. 

### Evidence 

![CountdownWithLed](images/LaunchPad2.gif)

### Wiring

![Simulation Wiring](images/LaunchPad2Wiring.png)

### Code

[Code for Launch pad 2](raspberry-pi/LaunchPad2.py)

### Reflection

I started the task by combining code from the LED blink and the countdown from Launch Pad 1. I figured it would be similar LED code but the difference is what the port I was using is. The final way I figured how to use the red then green leds was to have the green turn on using an "else:" statement only when the counter hit 0. I also had troubles with syntax errors, (capitalization of the word "True", needing to lowercase "value".)

### Assignment Description

Launch Pad Part 3: The third part of the launch pad combines the prior assigmment of the blinking LED with the countdown and adding a button to set off the sequence. 

### Evidence 

![ButtonVideo](images/LaunchPad3.gif)

### Wiring

![Simulation Wiring](images/LaunchPad3Wiring.png)

### Code

[Code for Launch pad 3](raspberry-pi/LaunchPad3.py)

### Reflection

This assignment was not as troubling as the previous one. I basically copied the LED code and replaced it with button variables and then added a "while True:" at the top of my main code to trump the rest unless the button is pressed. I also forgot to put the letter "t" in digitalio in one of my lines. The code given in the canvas embedded info was very helpful and basically gave it all to me. 

### Assignment Description

Launch Pad Part 4: The fourth part of the launch pad combines the prior assignment with the button starting the sequence with the addition of a servo turning from 0 degrees to 180 degrees upon liftoff.

### Evidence

![Servo Video](images/LaunchPad4.gif)

### Wiring

![4Wiring](images/LaunchPad4Wiring.png)

### Code

[Code with the Servo](raspberry-pi/LaunchPad4.py)

### Reflection

This assignment was basically just using the servo code given to me in the module of Launch Pad 4 and trying to implement the servo's features into the code. The biggest problem I had was the allignment of my code not fitting into the "If" statements. You need to have it indented past the "If" statement for it to take effect. 

## Raspberry_Pi_Crash_Avoidance

### Assignment Description

First part of crash avoidance. Accelerometer is only part utilized here, gives X/Y/Z values based on the movement of the board.

### Evidence

![Gif](images/CrashAvoidance1.gif)

### Wiring

![Wiring](images/CrashAvoidance1Wiring.png)

### Code

[Accelerometer Code](raspberry-pi/CrashAvoidance1.py)

### Reflection

Had to remember to put a "time.sleep(1)" at the end of my "while True:" statement, still had to import board and time.

### Assignment Description

Second part of crash avoidance. Accelerometer detects when it is at 90 degrees at an X or Y position and turns on an LED.

### Evidence

![Gif2](images/CrashAvoidance2.gif)

### Wiring

![Wiring](images/CrashAvoidance2Wiring.png)

### Code

[Detector Code](raspberry-pi/CrashAvoidance2.py)

### Reflection

Majority of this assignment was adding the led code previously learned into the previous acceleration code. Had issues trying to properly detect the X/Y values because I had the lines determining it stacked on top of each other instead of being in a straight line with only a colon at the end of it.

### Assignment Description

Crash Avoidance part 3. Combines part 2 and adds an OLED screen that displays X/Y/Z values in 3 decimal places as rad/s (radians per second)

### Evidence

![Gif3](images/CrashAvoidance3.gif)

### Wiring

![Wiring](images/CrashAvoidance3Wiring.png)

### Code

[OLED Code](raspberry-pi/CrashAvoidance3.py)

### Reflection

One part that simplified wiring was wiring the Pico's GP.. or 3v3 power pins to a whole channel then wiring the accelerometer/OLED to that channel. Used 'f strings' for first time which allows specific code to be printed within its boundaries. Used a 'round' function on either side of the gyro function to determine the decimal places to round to. 

### Assignment Description

Landing Area part 1. When inputting 3 sets of x,y coordinates into the terminal the code will give the area of the 3 given vertices, if given a letter input that is not a number it will display an error message and reset the command to prompt a new first coordinate.

### Evidence

![Gif1](images/LandingArea1.gif)

### Wiring

![LandingAreaWiring](images/LandingArea1Wiring.png)

### Code

[Area Code](raspberry-pi/LandingArea1.py)

### Reflection

Had trouble with the "try and except" function because I had left a line of example code in the function. Learned a couple new function such as the try and except and "split" function. 

### Assignment Description

Landing Area part 2 takes the area code from Landing Area 1 and displays the triangle created on the OLED.

### Evidence

![Gif2](images/LandingArea2.gif)

### Wiring

![Wiring](images/LandingArea2Wiring.png)

### Code

[OLED Area Code](raspberry-pi/LandingArea2.py)

### Reflection

Had to use i2c code and splash code for the OLED from Crash avoidance. Had trouble with placement of lines that define functions, needed to have them before the functions themselves. 

### Assignment Description

Morse code part 1 takes your input of text and converts it into morse code, if you type "-q" it will cancel the program

### Evidence

![Gif](images/MorseCode1.gif)

### Wiring

No wiring was necessary. 

### Code

[Morse Code](raspberry-pi/MorseCode1.py)

### Reflection

Morse code part 1 gives the translations of the letter to the morse code beforehand, except had to type in my own translation for the space bar. Used a "break" function for the first time which in comination with an "if" statement can break you out of a command, thus the "-q". Then had to transfer the words I put in to morse code with a variable. 

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!


&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Buy more stickers](https://www.amazon.com/Stickers-Grocery-Warning-Labels-Adhesive/dp/B08SLZMMVW/ref=sr_1_3?keywords=spicy+stickers&qid=1662053762&sr=8-3)

[Test.py](raspberry-pi/test.py)
### Test Image
![New spicy sticker](images/Spicy.jpg)
### Test GIF
![Scared spicy man](images/Spicy.gif)
