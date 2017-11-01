from deap import algorithms, base, benchmarks, tools, creator
from copy import deepcopy
import numpy

from toolbox import toolbox
from data import data
from score import getScoreVector

dataSet = data['nrp-e3']


# Store individuals in logbook
stats = tools.Statistics(key=lambda ind: ind.fitness.values)
stats.register("population", deepcopy)
stats.register("avgScore", numpy.mean, axis = 0)
stats.register("stdScore", numpy.std, axis = 0)
stats.register("minScore", numpy.min, axis = 0)
stats.register("maxScore", numpy.max, axis = 0)

def runGA(toolbox = toolbox, popSize = 50, maxGen = 10, mutProb = 0.1, stats = stats):
	toolbox.pop_size = popSize
	toolbox.max_gen = maxGen
	toolbox.mut_prob = mutProb

	pop = toolbox.population(n = toolbox.pop_size)
	pop = toolbox.select(pop, len(pop))

	# Run evolutionary algorithm
	# http://deap.readthedocs.io/en/master/api/algo.html#deap.algorithms.eaMuPlusLambda
	return algorithms.eaMuPlusLambda(
		pop,
		toolbox,
		mu = toolbox.pop_size,
		lambda_ = toolbox.pop_size,
		cxpb = 1 - toolbox.mut_prob,
		mutpb = toolbox.mut_prob,
		stats = stats,
		ngen = toolbox.max_gen,
		verbose = False
	)

def runRandom(toolbox = toolbox):
	currentGen = 0
	allGenerations = []
	fitnessesPerGen = []
	pop = toolbox.population(n = toolbox.pop_size)

	while currentGen < toolbox.max_gen:
		allGenerations.append(pop)

		fitnessesPerGen.append(
			list(toolbox.map(toolbox.evaluate, pop))
		)

		pop = toolbox.population(n = toolbox.pop_size)
		currentGen += 1


	return allGenerations, fitnessesPerGen
