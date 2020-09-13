#!/usr/bin/env python3
# NOTE: stdin-mode requires python3
#
# Simple program that allows setting led values via command line arguments or 
# stdin. If an argument string is passed via command line, the program runs 
# once, then exits. If no argument is passed, program accepts commands one line
# at a time until the command "exit" is sent. 
# 
# Accepts a comma separated list with the following allowed options:
# 
# [r/g/b]=[int] - red, green, blue (0-255), missing colour will be set to 0
# brightness=[int] - brightness percent (0-100)
# off - turns off the led. Sending this overrides any colour arguments.
# 
# Examples: 
# "r=255,b=100,brightness=50" - This sets the led to rgb(255, 0, 100)
# with 50% brightness. Blue is set to 0 because it was not in the string.
# "off" - Turns off the led.


import sys, re
# import apa102

#led = apa102.APA102(1, 15, 14, None, brightness=0.05)

def isAssignment(word):
    return re.match(r'^[a-z]+=[a-z0-9\.]+$', word);

# Converts string values to int values in range [minVal, maxVal], filling 
# missing keys with defaultVal 
def standardiseValue(values, key, minVal = 0, maxVal = 255, defaultVal = 0):
    numVal = int(values.get(key, str(defaultVal)))
    values[key] = max(minVal, min(numVal, maxVal))

# parses an input line into a dictionary.
def parseLine(line):
    words = line.split(',')
    values = {}
    for word in words:
        if word == 'off':
            return{'off': True}
        elif isAssignment(word):
            sides = word.split('=')
            values[sides[0]] = sides[1]

    standardiseValue(values, 'r')
    standardiseValue(values, 'g')
    standardiseValue(values, 'b')
    standardiseValue(values, 'brightness', 0, 100, 100)
    return values


#def setLed(values):
#    if values['off']:
#        led.set_pixel(0, 0, 0, 0)
#    else:
#        led.set_pixel(0, values.r, values.g, values.b, values.brightness)
#    led.show()

def setLedFromLine(line):
    values = parseLine(line)
    #setLed(values)
    print(values)

# If command line arguments exist, run once and exit
if len(sys.argv) == 2:
    setLedFromLine(sys.argv[1])
# Otherwise read commands one line at a time until an "exit" command is read 
else:
    for lineWithBreak in sys.stdin:
        line = lineWithBreak.replace('\n', '')
        if line == 'exit':
            break
        setLedFromLine(line)
