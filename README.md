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
