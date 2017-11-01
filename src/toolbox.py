from deap import algorithms, base, benchmarks, tools, creator
from numpy import dot
from random import randint

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
def getFitness(requirementVec = [], scoreVec = scoreVector, costVec = costVector):
	score = dot(scoreVec, requirementVec)
	cost = dot(costVec, requirementVec)

	return score, cost

toolbox.register('evaluate', getFitness)
toolbox.register('mate', tools.cxTwoPoint)
toolbox.register('mutate', tools.mutFlipBit, indpb = 0.05)
toolbox.register('select', tools.selNSGA2)

# Set GA parameters
toolbox.pop_size = 5
toolbox.max_gen = 2
toolbox.mut_prob = 0.1


# Make single objective toolbox, maximise fitness
creator.create('FitnessMax', base.Fitness, weights = (1.0,))
creator.create('SingleObjIndividual', list, typecode = 'd', fitness = creator.FitnessMax)

singleObjToolbox = base.Toolbox()
singleObjToolbox.register('attr_bool', randint, 0, 1)
singleObjToolbox.register('individual', tools.initRepeat, creator.SingleObjIndividual, singleObjToolbox.attr_bool, n = howManyRequirements)
singleObjToolbox.register('population', tools.initRepeat, list, singleObjToolbox.individual)

# Fitness Function
def getSingleFitness(requirementVec = [], scoreVec = scoreVector, costVec = costVector):
	score = dot(scoreVec, requirementVec)
	cost = dot(costVec, requirementVec)

	return score / cost

singleObjToolbox.register('evaluate', getSingleFitness)
singleObjToolbox.register('mate', tools.cxTwoPoint)
singleObjToolbox.register('mutate', tools.mutFlipBit, indpb = 0.05)
# singleObjToolbox.register('select', tools.selNSGA2)
