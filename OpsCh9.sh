#!/bin/bash
#Lets create a script that would work like a DDOS attack by using a while loop
#In this script we want to contiune to ping our personal pc in a infitine while loop
#Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash

# while [ true ]; do
#     ping "8.8.8.8"
# done
# To End the loop try pressing control z or control c
# Stretch Goal:
# Can you do this with an until loop to have it execute a specfic number of times?

counter=0

until [ $counter -gt 5 ];do
    echo $counter
    ((counter++))
done
