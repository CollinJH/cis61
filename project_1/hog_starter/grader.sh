#!/bin/bash
#
#script to easily run select question grader


run_grader() {
  python3 hog_grader.py -q "$1" 
}

if [ $# -eq 0 ]; then
  echo "Please provide an argument."
  exit 1
fi

run_grader "$1"
