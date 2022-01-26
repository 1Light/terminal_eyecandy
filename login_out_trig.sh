#!/bin/bash

dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | \
( while true
    do read X
    if echo $X | grep "boolean true" &> /dev/null; then
        echo "locking at $(date)" >> $HOME/logs/time_xprofile
    elif echo $X | grep "boolean false" &> /dev/null; then
        echo "unlocking at $(date)" >> $HOME/logs/time_xprofile
        bash 
    fi
    done )
