#type: ignore
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}
modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier
    #variables to make life easier
while True:
    print("Enter message for morse code, or enter -q to quit")
    message = input()
    # working of upper() function
    print("\nConverted String:")
    if message == "-q":
        break
    message = message.upper()
    variable = " "
    for letter in message: 
        variable = variable + (MORSE_CODE[letter]) + " "
    # message is just my input, for letter in message means it will print each individual letter, but I want to convert each letter to morse code 
        #print(variable)
        #This does not work for some reason
    # use MORSE_CODE[letter] here to translate from input into morse code
    for character in variable: 
        print(character)
        #Mr. Miller does not know why this works and why print variable and print character breaks it
        if character == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(between_taps)
        if character == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(between_taps)
        if character == " ":
            time.sleep(between_letters)
        if character == "/":
            time.sleep(between_words)
        #variables used to determine time for the led to stay on and off