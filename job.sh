#!/bin/bash
. $(dirname "$0")/URL.sh
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "job.sh has been entered"
python3 $DIR/main.py $URL
