# multi-objective-optimisation

Suppose we're developing a software, we have a list of requirements,
their costs and a list of customers with desired requirements ordered by wishes.
Each customer has a weight. Each requirement has a cost and score. Using a genetic algorithm
this project is trying to find solutions using NSGA2 selection.
Trying to minimise cost and maximise score.

Using the [DEAP](https://github.com/DEAP/deap) Evolutionary Algorithms Python library.
Main paper for reference: [Deb et al.](http://ieeexplore.ieee.org/document/996017/)
Reference for [DEAP multi-objective-optimisation](https://github.com/lmarti/evolutionary-computation-course/blob/master/AEC.06%20-%20Evolutionary%20Multi-Objective%20Optimization.ipynb)

## To Run:
### 1. Install [pipenv](https://github.com/kennethreitz/pipenv)
```bash
$ pip install pipenv
```

### 2. cd to project directory and:
```bash
$ pipenv install
```

```bash
$ pipenv shell
```
```bash
$ python src/geneticAlgorithm.py
```
Wait for the GA to run, you'll see an [animation](https://youtu.be/xeNv6VDH004) at the end.

#### If you prefer using Anaconda:
You'll need to install [DEAP](https://github.com/DEAP/deap) globally:
```bash
$ conda install -c conda-forge deap
```

cd to project directory and:

```bash
$ python src/geneticAlgorithm.py
```

✨🍰✨
