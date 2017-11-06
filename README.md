# multi-objective-optimisation
![animation of improving generations](https://media.giphy.com/media/xUOxeZiPQZXuw3MMU0/giphy.gif)


Suppose we're developing a software, we have a list of requirements,
their costs and a list of customers with desired requirements ordered by wishes.
Each customer has a weight. Each requirement has a cost and score. Using a genetic algorithm
this project is trying to find solutions using NSGA2 selection.
Trying to minimise cost and maximise score.

This repo comes with a complementary [report](VladyVeselinov-ATSE-Assignment3.pdf).

Using the [DEAP](https://github.com/DEAP/deap) Evolutionary Algorithms Python library.
Main paper for reference: [Deb et al.](http://ieeexplore.ieee.org/document/996017/)
Reference for [DEAP multi-objective-optimisation](https://github.com/lmarti/evolutionary-computation-course/blob/master/AEC.06%20-%20Evolutionary%20Multi-Objective%20Optimization.ipynb)

## To Run:
### 1. Install [pipenv](https://github.com/kennethreitz/pipenv)
```bash
$ pip install pipenv
```

### 2. Cd to project directory and:
```bash
$ pipenv install
```

```bash
$ pipenv shell
```

1. To see a plot comparing random, single objective and multi-objective:

```bash
$ python src/plot.py
```

2. To see the animation:
```bash
$ python src/animation.py
```

#### If you prefer not to use pipenv:
You'll need to install [DEAP](https://github.com/DEAP/deap) globally:
```bash
$ pip install deap
```
or using [Conda](https://github.com/conda/conda)
```bash
$ conda install -c conda-forge deap
```

Cd to project directory and:
1. To see a plot comparing random, single objective and multi-objective:

```bash
$ python src/plot.py
```

2. To see the animation:
```bash
$ python src/animation.py
```
✨🍰✨
