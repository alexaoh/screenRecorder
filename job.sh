#!/bin/bash
. $(dirname "$0")/URL.sh
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "job.sh has been entered"

if [ $# -eq 1 ]
  then
    echo "Going to record for $1 minutes."
    python3 $DIR/main.py $URL
  else
    echo "No arguments supplied. Need amount of minutes to record for."
fi
