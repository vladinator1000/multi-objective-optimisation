from deap import algorithms, base, benchmarks, tools, creator

from toolboxes import nsgaToolbox, statsGen
from data import data

dataSet = data['nrp1']

def runGA(toolbox = nsgaToolbox, popSize = 50, maxGen = 10, mutProb = 0.1, stats = statsGen):
	pop = toolbox.population(n = popSize)
	pop = toolbox.select(pop, len(pop))

	# Run evolutionary algorithm
	# http://deap.readthedocs.io/en/master/api/algo.html#deap.algorithms.eaMuPlusLambda
	return algorithms.eaMuPlusLambda(
		pop,
		toolbox,
		mu = popSize,
		lambda_ = popSize,
		cxpb = 1.0 - mutProb,
		mutpb = mutProb,
		stats = stats,
		ngen = maxGen,
		verbose = False
	)

def runRandom(toolbox = nsgaToolbox, popSize = 50, maxGen = 10):
	currentGen = 0
	allGenerations = []
	fitnessesPerGen = []

	# Use toolbox only to generate population
	population = toolbox.population(n = popSize)

	while currentGen < maxGen:
		allGenerations.append(population)

		fitnessesPerGen.append(
			list(toolbox.map(toolbox.evaluate, population))
		)

		population = toolbox.population(n = popSize)
		currentGen += 1


	return allGenerations, fitnessesPerGen
