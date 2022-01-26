#!/bin/bash

hour=$(date +"%H")

if [ $hour -ge 6 -a $hour -lt 12 ]
then
    greet="Good Morning, $USER"
elif [ $hour -ge 12 -a $hour -lt 18 ] 
then
    greet="Good Afternoon, $USER"
elif [ $hour -ge 18 -a $hour -lt 23 ]  
then
    greet="Good evening, $USER"
else
    greet="What the Hell ,$USER . You should not be using computer this late."
fi
    
# display greet
echo $greet | festival --tts &
