# Controller script for pimoroni fanshim led

This is a simple script to set the color, brightness and on/off-state of the led on the pimoroni fan-shim. The script can be run in two ways, either by passing input via command line arguments or by repeatedly reading commands via standard input. To edit the led states you need to run as root and it's advised that you run the regular fanshim service with the `--noled option` so that the led is free to use.

