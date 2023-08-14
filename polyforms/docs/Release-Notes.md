# Release Notes

## Release 0.1.0 

**Release Date:** August 6, 2023

* The following modules are created within the `polyforms` package: 
    * `n_gon.py`, `backtrackk.py` -- list magic/perfect polyiamonds for the given permutation. 
      A context manager is used to allow directing output to a file or printing it to a console.
    * `geom_utilities.py` -- polygon functions using the regular 2D coordinates. 
    * `point_tg.py`, `poly_geometry.py` -- polygon functions using the triangle grid coordinates.
    * `seq_storage.py` -- an interface to access perfect polyiamond sequences and other notable reference data. 
    * `magic_enum.py` -- a module to list polyiamonds satisfying certain filtering conditions (or searching for 
      maxima and minima). It is a user-friendly wrapper around `n_gon.py` to find just the polyiamonds you need.
      It uses an iterator for all magic polyamond permutations (omitting the symmetric ones).
    * `draw_scene.py` -- a module to draw polyiamond pictures with Matplotlib.
* Some Jupyter Notebook examples.
