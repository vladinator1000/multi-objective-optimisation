from deap import algorithms, base, benchmarks, tools, creator
from random import randint
from numpy import dot


from data import data
from score import getScoreVector

dataSet = data['nrp3']


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

# This is the fitness function
def getScoreAndCost(requirementVec = [], scoreVec = scoreVector, costVec = costVector):
	score = dot(scoreVec, requirementVec)
	cost = dot(costVec, requirementVec)

	return score, cost

toolbox.register('evaluate', getScoreAndCost)
toolbox.register('mate', tools.cxTwoPoint)
toolbox.register('mutate', tools.mutFlipBit, indpb = 0.05)
toolbox.register('select', tools.selNSGA2)

# Initialise population with 'n' size
population = toolbox.population(n = 10)


# Run the Genetic Algorithm
for gen in range(10):
	# Crossover and Mutation
	offspring = algorithms.varAnd(population, toolbox, cxpb = 0.9, mutpb = 0.1)

	# Evaluate Fitnesses
	fitnesses = toolbox.map(toolbox.evaluate, offspring)

	# Assign fitness to each individual in offspring
	for fit, ind in zip(fitnesses, offspring):
		ind.fitness.values = fit

	# Selection
	population = toolbox.select(offspring, k = len(population))

