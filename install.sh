#!/bin/bash
rm -f /usr/local/bin/fanshimled
if [ "$1" != "-r" ]; then 
    cp ledController.py /usr/local/bin/fanshimled
fi
