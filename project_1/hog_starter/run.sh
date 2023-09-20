#!/bin/bash
#
# script to run final strategy 10 times


for ((i = 0; i <= 10; i++)); do
  python3 hog.py -r
done

