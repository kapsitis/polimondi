# Polyforms package

## Purposes of the package

* Library to enumerate polyiamonds with the ability to extend conditions.
* Library to find polyiamond pairs with close editing distances.
* Library to compute geometric properties of a given polyiamond. 
* Library to draw vector-graphic pictures on triangle grid.
* Static data representing some useful families of polyiamonds.


# Setting up the environment

It seems that `base` is already installed as you install Conda.
Later on you can list all the environments, deactivate the current environment and finally - activate the 
virtual environment you need: 

```
conda info --envs
# OR just "conda env list"
conda deactivate
conda activate base
```

Once your Conda environment is activated you can use pip to show the packages currently installed. 
You also can uninstall the (previous) version of `polyforms` and install the newest one from a Wheel file. 

```
conda list
pip list | grep polyforms
pip uninstall polyforms
pip install dist/polyforms-0.1.0-py3-none-any.whl
```



Install a package in development (editable) mode:

```
cd polyforms
pip uninstall polyforms
pip install -e .
```

Unlike installing a wheel file, this enables to do edits in this directory - and they are immediately effective 
without reinstalling the package. 
We assume that the directory "polyforms" contains "src" subdirectory. 


```
pip uninstall -y polyforms
pip install --editable ../
```


# Making a new "polyforms" release

Before creating a new release, you need to run all the unit tests like this: 

```
cd polyforms/tests
pytest
# Sometimes you may want to test just one pytest file:
pytest test_poly_gemoetry.py 
# Or even a single test method in that file:
pytest test_poly_gemoetry.py::test_long_perimeter_points
```

You also may want to edit a file `docs/Release-Notes.md` -- just explain what has been 
added to the package since last release. 


After that you can tag the release like this:

```
git tag v0.1.0
git push --tags
```

In the version number `v0.1.0` the first digit (0) is the major release number (reserved if there
are major refactorings or fundamentally new features); the second digit (1) is the minor release number 
(any time you add some change in functionality). The last digit (0) is for hotfixes, if we
do not want to change the functionality, just to fix some mistakes introduced during a major or 
minor release. 

Then use Poetry to create a Wheel package and publish it back to Git: 

```
cd polymonds
rm -fr dist
poetry build

```







Yes, in Python it is possible to make a comparison like `out_func == print` to check if the 
output is going to the console or a file. However, keep in mind this only works if `out_func` 
is directly assigned the `print` function, not when it's assigned a different function that happens to use `print`.

That being said, it's usually not the best practice to rely on comparing functions to determine 
behavior in this way, as it can lead to confusing and error-prone code.

In this case, rather than checking whether `out_func == print`, a more idiomatic Python solution 
might be to use a context manager, which can handle the file cleanup for you, whether 
you're using `print` or writing to a file. Here's an example:

```python
from contextlib import contextmanager

@contextmanager
def output_function(out_func=print, filename=None):
    if filename:
        file = open(filename, 'a')
        yield file.write
        file.close()
    else:
        yield out_func

def list_polyforms(n, out_func=print, filename=None):
    with output_function(out_func, filename) as do_output:
        # Now use do_output instead of out_func or print
        for i in range(n):
            do_output(str(i))

list_polyforms(5, filename='my_output.txt')
```

In this code, `output_function` is a context manager that will handle opening and closing the file 
(if a filename is provided). This allows your `list_polyforms` function to just use this context 
manager's output function (`do_output`) without worrying about whether it's using 
`print` or writing to a file, as the context manager takes care of file cleanup.






