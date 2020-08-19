#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "record.sh has been entered"
python3 $DIR/record.py
