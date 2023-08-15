#!/bin/bash

for nb in *.ipynb; do jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True --inplace "$nb"; done
