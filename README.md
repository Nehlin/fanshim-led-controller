# Controller script for pimoroni fanshim led

This is a simple script to set the color, brightness and on/off-state of the led on the pimoroni fan-shim. The script can be run in two ways, either by passing input via command line arguments or by repeatedly reading commands via standard input. To edit the led states you need to run as root and it's advised that you run the regular fanshim service with the `--noled option` so that the led is free to use.

## Usage

The script accepts input as a single line with comma separated values. Missing values will be set to default. The possible values are:
- `r=[0, 255]` (default: 0) - red
- `g=[0, 255]` (default: 0) - green
- `b=[0, 255]` (default: 0) - blue
- `brightness=[0, 100]` (default: 100) - brightness, in percent
- `off` - ignores other commands and turns the led off

Examples: 
- `r=255,g=100,b=20,brightness=70` - rgb(255, 100, 20), with 70% brightness
- `off` - turns off the led.

There are two ways of interacting with the script. If launched vith the input string as a command line argument, the script will execute that string once, then terminate. If launched without command line options, the script will contiuously accept commands via standard input until an `exit` command is written.

### command line mode:
`sudo ./ledController.py r=250` - sets the controller to red with 100% brighness, then exits.


### stdin mode:
`sudo ./ledController.py`

