#!/bin/bash
while true
do
  echo "Pick a number:"
  echo "1. Say 'Hello, World!'"
  echo "2. Ping Google"
  echo "3. Show network info"
  echo "Press anything else to quit."
  read choice
  if [ "$choice" = "1" ]; then
    echo "Hello, World!"
  elif [ "$choice" = "2" ]; then
    ping -c 2 google.com
  elif [ "$choice" = "3" ]; then
    ifconfig
  else
    echo "Goodbye!"
    break
  fi
done
