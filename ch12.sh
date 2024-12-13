#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

# echo "How is your day going? (good/bad)"
read -p "How was your day?" ANSWER

while [ true ]; do
  case $ANSWER in
  good | Good -
    echo -n "thats great to hear, keep it up!"
    break
    ;;

  bad | Bad
    echo -n "sorry to heat that, tomorrow is a new day."
    ;;
  *)
    echo "I didnt understand that, please respond with 'good' or 'bad'"
    ;;
esac
