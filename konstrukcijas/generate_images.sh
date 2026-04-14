#!/bin/bash

export PYTHONPATH="$PYTHONPATH:.."
# pytest tests/test_draw_scene.py
python make_images/make_figures_obtuse.py
