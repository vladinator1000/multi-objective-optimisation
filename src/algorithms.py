from deap import algorithms, base, benchmarks, tools, creator
from random import randint
from numpy import dot
from matplotlib import pyplot
from copy import deepcopy

from data import data
from score import getScoreVector

dataSet = data['nrp-e3']

scoreVector = getScoreVector(dataSet)
costVector = dataSet['requirementCosts']
howManyRequirements = len(costVector)


# Create a fitness Type,
# maximise first (score), minimise second (cost) element
creator.create('FitnessMaxMin', base.Fitness, weights = (1.0, -1.0))

# Create an Individual type that will have the fitness declared above
creator.create('Individual', list, typecode = 'd', fitness = creator.FitnessMaxMin)

# Make functions that will be called later,
# first argument is name of the function being declared
toolbox = base.Toolbox()

# Each solution will be made up of bools
toolbox.register('attr_bool', randint, 0, 1)

# and will be 'n' elements long
toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, n = howManyRequirements)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

# Fitness Function
def getScoreAndCost(requirementVec = [], scoreVec = scoreVector, costVec = costVector):
	score = dot(scoreVec, requirementVec)
	cost = dot(costVec, requirementVec)

	return score, cost

toolbox.register('evaluate', getScoreAndCost)
toolbox.register('mate', tools.cxTwoPoint)
toolbox.register('mutate', tools.mutFlipBit, indpb = 0.05)
toolbox.register('select', tools.selNSGA2)

# Set GA parameters
toolbox.pop_size = 50
toolbox.max_gen = 1000
toolbox.mut_prob = 0.1

# Store individuals in logbook
stats = tools.Statistics()
stats.register("pop", deepcopy)

def runGA(toolbox = toolbox, stats = stats, verbose = False):
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
		verbose = verbose
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

# TODO single objective
