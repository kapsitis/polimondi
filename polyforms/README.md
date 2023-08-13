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




```python
from polyforms.mag_enum import MagEnum
from polyforms.n_gon import Format

def main():
    n = 5
    permutation = list(range(1,n+1))
    permutation.reverse()
    me = MagEnum(Format.LETTERS)
    me.list_iamonds(permutation)

if __name__ == '__main__':
    main()
```


# Instrukcijas Windows mašīnai

## Anaconda instrukcijas

Anaconda ir viena no čūsku iedvesmotajām valodas Python vidēm; tajā labi darbojas arī Jupyter Notebook; 
var vienlaikus darbināt dažādas Python versijas un vides, kas cita citai netraucē. 

1. Uzstāda Anaconda vidi (tā ir PowerShell vide ar Python).
   [https://docs.anaconda.com/free/anaconda/install/windows/]
2. Atver Anaconda termināli: **Start > Anaconda3 (64 bit) > Anaconda Prompt**. 
3. Terminālī var ierakstīt komandu `python` un izpildīt tur dažas komandas.

Var ievērot, ka Anaconda "neatceras" tās pakas, kas ir uzstādītas citās Python vidēs
(piemēram PyCharm). Pašai Anaconda ir virtuālā vide (pilna Python saimniecība), 
kas saucas "base". To var aktivēt un deaktivēt. Ja tā ir aktivēta, tad termināļa lodziņā 
visu laiku parādās vārds "(base)" rakstīts iekavās.


## Poetry rīks

Poetry ļauj taisīt pašiem savas Python pakotnes. Mums pagaidām noder viena šāda pakotne - "polyforms". 
Tur ir par polimondiem un, iespējams, nākotnē varētu būt vēl citas figūriņas, kas saliktas no vienādiem 
gabaliņiem - kvadrātiņiem, sešstūrīšiem, kubiņiem.

1. Atver Android termināli, uzstāda tajā Python pakotņu pārvaldības rīku `poetry`: 
   ```
   curl -sSL https://install.python-poetry.org | python -
   ```
2. Aiziet uz polyforms; izpilda `poetry install`
3. Tad palaiž `poetry shell`
4. Ja grib uzzināt, kur ir Python virtuālā vide, kurā ieinstalējusies jaunā pakotne:
   `poetry env info --path`
5. Darbina vienības testus: 
   ```
   cd tests
   pytest
   # Ja gribas palaist vienu atsevišķu (pašai savu) testa failiņu:
   pytest test_mytests.py
   #  (vai pat var palaist vienu metodi)
   pytest test_mytests.py#test_abc
   
   # Parasti vienības testi nedrukā tās print komandas, kas tiek izsauktas testos un viņu funkcijās.
   # Bet, ja gribas redzēt izdrukāto informāciju:
   pytest -s test_mytests.py
   ```


# Jupyter Notebook

1. Aiziet uz apakšdirektoriju `docs`, palaiž `jupyter notebook`
2. Pārlūkprogrammā pagaida, kamēr jaunā cilne (tab) atveras - redzami `docs` direktorijā esošie faili.
3. Atver kādu no `ipynb` failiem. 






`poetry shell`

This spawns a shell with the virtual environment activated.

If you want to know the path to the virtual environment that Poetry has created, use:

`poetry env info -p`

or

 
