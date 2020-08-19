#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "record.sh has been entered"

if [ $# -eq 1 ]
  then
    echo "Going to record for $1 minutes."
    python3 $DIR/record.py $1 
  else
    echo "No arguments supplied. Need amount of minutes to record for."
fi
