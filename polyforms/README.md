# Polyforms package

## Purposes of the package

* Library to enumerate polyiamonds with the ability to extend conditions.
* Library to find polyiamond pairs with close editing distances.
* Library to compute geometric properties of a given polyiamond. 
* Library to draw vector-graphic pictures on triangle grid.
* Static data representing some useful families of polyiamonds.


# Some 3.8 Python notes

```buildoutcfg
cd konstrukcijas/editing_distance
export PYTHONPATH="../../polyforms/src"
python poly_perfect_lists.py 13

nohup python perfect_extremes_parallel.py perfect 25 width

ps -ef | grep parallel
jobs


du -sh /home/kalvis
df 

```



grep "^ABA" perfect_24.txt | wc
 1655084 1655084 41377100
grep "^ABC" perfect_24.txt | wc
 1976710 1976710 49417750
grep "^ABD" perfect_24.txt | wc
 1560193 1560193 39004825
grep "^ABF" perfect_24.txt | wc
 1751151 1751151 43778775
grep "^ACA" perfect_24.txt | wc
 1858038 1858038 46450950
grep "^ACB" perfect_24.txt | wc
 1867195 1867195 46679875
grep "^ACD" perfect_24.txt | wc
 1412787 1412787 35319675
grep "^ACE" perfect_24.txt | wc
  539868  539868 13496700

1655084 + 1976710 + 1560193 + 1751151 + 1858038 + 1867195 + 1412787 + 539868
12621026


## n = 25

Total polyiamonds found: 35662687
[1017696, 1520413, 1120012, 1050761, 1058979, 1375118, 1918028, 1288091, 1580584, 1706631, 646748, 287784, 1210590, 1277438, 1066756, 1578034, 1370096, 1631126, 942032, 1235502, 1005663, 1724213, 1837993, 887874, 1245346, 1451309, 912743, 221520, 0, 1087833, 405774, 0]

Metric = width
[(1, 1), (44, 1), (23, 2), (169, 3), (1, 6), (2, 18), (20, 1), (63, 6), (2, 1), (4501, 1), (1, 4), (2, 25), (19, 1), (1, 2), (33, 1), (2162, 13
), (2, 1), (11, 1), (1, 6), (4, 4), (1, 1), (1, 1), (2, 5), (4, 1), (1, 10), (8, 1), (1, 1), (2, 1), (0, 0), (1, 1), (9, 13), (0, 0)]

 

# Pastmarka - 1
grep -Er "^A(CA)*(EA)*(EC)*(AC)*$" --include="acute_*.txt"
acute_27.txt:ACAEAEAECECECECECACACACACAC
acute_35.txt:ACACAEAEAEAECECECECECECECACACACACAC

# Pastmarka - 2
grep -Er "^A(CA)*(CE)*(AE)*(AC)*$" --include="acute_*.txt"
./acute_9.txt:ACECEAEAC

# Gandrīz Pastmarka - 2b
grep -Er "^A(CA)*(CE)*(AE)*CE(AE)*(AC)*$" --include="acute_*.txt"
./acute_33.txt:ACACACECECECEAEAECEAEAEAEAEACACAC
./acute_39.txt:ACACECECECEAECEAEAEAEAEACACACACACACACAC
./acute_57.txt:ACACACACACECECECECECECEAEAEAEAEAEAEAECEAEAEAEAEACACACACAC

# Gandrīz Pastmarka - 2bc
grep -Er "^A(CA)*(CE)*(AE)*CE(AE)*(AC)*AE(AC)*$" --include="acute_*.txt"








def main(n):
    prefixes = ['ABA', 'ABC', 'ABD', 'ABE', 'ACA', 'ACB', 'ACD', 'ACE']
    for prefix in prefixes:
        q = NGonProblem(n, list(range(n, 0, -1)), prefix, Format.COMPACT, FileWriter(f'perfect_{n}_{prefix}.txt'))
        b = Backtrackk(q)
        while b.attempt(0):
            q.display()
        print(f'Found {q.solution_count} polyiamonds')







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


# Cleaning out notebook files

```
for nb in *.ipynb; do jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True --inplace "$nb"; done
```

or 

```
pip install nbstripout
nbstripout your_notebook.ipynb
```

and also add this as a Github filter.

```bash
nbstripout --install
```
This will ensure that outputs are stripped from your notebooks each time you commit to your repository.

# Procedure: Using Google Colab

1. Visit an URL like this: [https://drive.google.com/drive/my-drive]. Connect to "My Drive"
2. Upload the wheel file e.g. `polyforms-0.1.0-py3-none-any.whl` to that drive (subdirectory `packages`)
3. Mount the drive (if it asks for permissions, agree)
```
from google.colab import drive
drive.mount('/content/drive')
```
4. Install the package:
```
!pip install '/content/drive/MyDrive/Colab Notebooks/polyforms-0.1.0-py3-none-any.whl'
```
5. Upload some script like this:
```python
from polyforms.draw_scene import *
from polyforms.perfect_seq import *
from polyforms.polyiamond import Polyiamond
import numpy as np

p1 = Polyiamond('ACEDF')
scene = DrawScene(Align.BASELINE)
scene.add_polyiamond('p1', p1)

scene.pack()
scene.show_grid()
(off_x, off_y) = scene.get_offset('p1')

perimeter = p1.list_perimeter()
perimeter2d = [pp.get_xy() for pp in perimeter]
for (x,y) in perimeter2d:
    scene.ax.plot(x+off_x, y, marker='o', color='blue')

scene.set_size_in(6,3)
```
6. Run this and observe the image.







# Procedure: How to create a new "polyforms" release

**Step 1 (Unit tests):**  
Before creating a new release, you need to run all the unit tests like this:  
```bash 
cd polyforms/tests
pytest
```

If something fails, you may want to run one pytest file or even one method in a testfile:
```bash
pytest test_poly_gemoetry.py 
pytest test_poly_gemoetry.py::test_long_perimeter_points
```

**Step 2 (System/Jupyter tests):**  
Do some of the above experiments -- check that Jupyter notebooks 
under `polyforms/docs` can run. They should also 


**Step 3 (Update Release Notes):**  
Edit the file `docs/Release-Notes.md` -- explain what has been 
added to the package since last release, error fixes and other improvements. 


**Step 4 (Check in and tag):** 
Check all the code in repository.
After that you can tag the release like this:  
```bash
git status
# If status is not empty; keep adding files (or remove dependent files)
# After everything locally is clean, commit with a message:
git commit -m "Release v0.1.0-beta2"
git tag v0.1.0-beta2
git push --tags
```

**Note:**  
In the version number `v0.1.0` the first digit (0) is the major release number (reserved if there
are major refactorings or fundamentally new features); the second digit (1) is the minor release number 
(any time you add some change in functionality). The last digit (0) is for hotfixes, if we
do not want to change the functionality, just to fix some mistakes introduced during a major or 
minor release. 

**Step 5 (Build Wheel file):**  
Use Poetry to create a Wheel package and publish it back to Git: 

```bash
cd polymonds
rm -fr dist
poetry build
```

**Step 6 (Publish the release):** 

* Navigate to the main page of the repository in GitHub.
* Click the `releases` link.
* Click `Create a new release`.
* In the `Tag version` field, type the version (such as `v0.1.0-beta2`)
* Type a title and description for the release.
* Click `Attach binaries by dropping them here or selecting them`, and upload your `polyforms-0.1.0.tar.gz` and `polyforms-0.1.0-py3-none-any.whl` files.
* Click `Publish release`.




# Note: Using Different output streams

Sometimes you need to have flexible output from your polymond methods
(for example, to decide, if they will write to a file or print to a console). 

If you need to have flexibility (which output stream to use), 
one can employ a "context manager", which can handle the file cleanup for you, whether 
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



## Deprecated Stuff


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

