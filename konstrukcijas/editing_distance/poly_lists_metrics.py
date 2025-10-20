import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '../../polyforms/src'))
sys.path.insert(0, parent_dir)

from polyforms.n_gon import NGonProblem
from polyforms.n_gon import FileWriter
from polyforms.n_gon import Format
from polyforms.backtrackk import Backtrackk
from multiprocessing import Pool, cpu_count
from polyforms.polyiamond import Polyiamond

def read_as_list(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    return lines

def display_area(s):
    pp = Polyiamond(s)
    print(f'area({s}) is {pp.get_area()}')



def main(filename):
    lines = read_as_list(filename)
    min = 1000000
    max = 0
    currmin = "NA"
    currmax ="NA"
    for line in lines:
        line = line.strip()
        pp = Polyiamond(line)
        arr =pp.get_area()
        if arr < min: 
            min = arr
            currmin = line
        if arr > max:
            max = arr
            currmax = line
    return (currmin, currmax)

if __name__=='__main__':
    filename = sys.argv[1]
    currmin, currmax = main(filename)
    if currmin == "NA" or currmax == "NA": 
        print(f"No results in {filename}")
    print(f"({currmin}, {Polyiamond(currmin).get_area()})")
    print(f"({currmax}, {Polyiamond(currmax).get_area()})")
