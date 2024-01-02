#!/bin/bash

echo "Processing ${1}-polyiamonds:"

/Users/kapsitis/opt/anaconda3/bin/python perfect_extremes_parallel.py perfect "$1" area
/Users/kapsitis/opt/anaconda3/bin/python best_prefixes.py perfect "$1" area
/Users/kapsitis/opt/anaconda3/bin/python perfect_extremes_parallel.py perfect "$1" diameter
/Users/kapsitis/opt/anaconda3/bin/python best_prefixes.py perfect "$1" diameter
/Users/kapsitis/opt/anaconda3/bin/python perfect_extremes_parallel.py perfect "$1" dimension
/Users/kapsitis/opt/anaconda3/bin/python best_prefixes.py perfect "$1" dimension
/Users/kapsitis/opt/anaconda3/bin/python perfect_extremes_parallel.py perfect "$1" width
/Users/kapsitis/opt/anaconda3/bin/python best_prefixes.py perfect "$1" width



