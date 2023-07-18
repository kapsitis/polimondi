# Polyforms package

## Purposes of the package

* Library to enumerate polyiamonds with the ability to extend conditions.
* Library to find polyiamond pairs with close editing distances.
* Library to compute geometric properties of a given polyiamond. 
* Library to draw vector-graphic pictures on triangle grid.
* Static data representing some useful families of polyiamonds.

## Notes

These commands are used to build package (and to install in pip). 

```
virtualenv env
source env/bin/activate
```

pip uninstall -y polyforms
pip install ../polyforms/dist/polyforms-0.1.0-py3-none-any.whl
```


```
python setup.py sdist bdist_wheel
pip install dist/polyforms-0.1-py3-none-any.whl
```


# Development mode (Editable) install

```
pip uninstall -y polyforms
pip install --editable ../
```


# Making a new release

git tag v0.1.0
git push --tags
Create new release. 







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