# hughes-random information

The 'hughes-random' project contains a package 'hughes' and the module 'random' containing the class 'RanDist' for the generation of random numbers from a user specificed distribution.

## 'hughes' package

### Installation & Quick Start:

The package can be installed by downloading a local copy  of 'hughes-random' then at command line by cd'ing into the parent folder 'hughes-random' and installing with:

> \ ..\hughes-random> python setup.py install

However, the easiest way to install a package is using github.

The package 'hughes' containing random.RanDist() can be installed from GitHub at command line on a machine with python, the required python packages (numpy, matplotlib.pylab) and git installed using pip and the command:

> \ ..\user> pip install git+https://github.com/Huggies23/hughes-random.git

The RanDist() class may then be used as followed in a python interpreter:

```
import hughes.random as hug

x = hug.RanDist(1000)
x.summary()
x.hist()
```
### hughes.random.RanDist()

All information on the RanDist() class (arguments, attributes and methods) can be found using:
```
import hughes.random
help(hughes.random.RanDist)
```
in a python 3.x interpreter.
