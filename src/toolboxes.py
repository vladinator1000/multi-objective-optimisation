from deap import algorithms, base, tools, creator
from random import randint
from copy import deepcopy
import numpy

from data import data
from score import getScoreVector

dataSet = data['nrp1']

scoreVector = getScoreVector(dataSet)
costVector = dataSet['requirementCosts']

# NSGA2 toolbox

# Create a fitness Type,
# maximise first (score), minimise second (cost) element
creator.create('FitnessMaxMin', base.Fitness, weights = (1.0, -1.0))

# Create an Individual type that will have the fitness declared above
creator.create('Individual', list, typecode = 'd', fitness = creator.FitnessMaxMin)

nsgaToolbox = base.Toolbox()

# Make functions that will be called later,
# first argument is name of the function,
# second is the actual function being called,
# all arguments after are passed to function being called

# Each solution will be made up of bools
nsgaToolbox.register('attr_bool', randint, 0, 1)

# and will be 'n' elements long
nsgaToolbox.register('individual', tools.initRepeat, creator.Individual, nsgaToolbox.attr_bool, n = len(costVector))
nsgaToolbox.register('population', tools.initRepeat, list, nsgaToolbox.individual)

# Fitness Function
def getFitness(requirementVec = [], scoreVec = scoreVector, costVec = costVector):
	score = numpy.dot(scoreVec, requirementVec)
	cost = numpy.dot(costVec, requirementVec)

	return score, cost

nsgaToolbox.register('evaluate', getFitness)
nsgaToolbox.register('mate', tools.cxTwoPoint)
nsgaToolbox.register('mutate', tools.mutFlipBit, indpb = 0.05)
nsgaToolbox.register('select', tools.selNSGA2)


# Make a single objective toolbox
creator.create('FitnessMax', base.Fitness, weights = (1.0,))
creator.create('SingleObjIndividual', list, typecode = 'd', fitness = creator.FitnessMax)

singleObjToolbox = base.Toolbox()
singleObjToolbox.register('attr_bool', randint, 0, 1)
singleObjToolbox.register('individual', tools.initRepeat, creator.SingleObjIndividual, singleObjToolbox.attr_bool, n = len(costVector))
singleObjToolbox.register('population', tools.initRepeat, list, singleObjToolbox.individual)

# Fitness Function
def getSingleFitness(requirementVec = [], scoreVec = scoreVector, costVec = costVector):
	score = numpy.dot(scoreVec, requirementVec)
	cost = numpy.dot(costVec, requirementVec)

	# Return a sequence with one element
	return score / cost,

singleObjToolbox.register('evaluate', getSingleFitness)
singleObjToolbox.register('mate', tools.cxTwoPoint)
singleObjToolbox.register('mutate', tools.mutFlipBit, indpb = 0.05)
singleObjToolbox.register('select', tools.selTournament, tournsize = 3)

# Export stats objects
statsGen = tools.Statistics()
statsGen.register('allGenerations', deepcopy)

# Needs to be passed population of fitnesses
statsFit = tools.Statistics()
statsFit.register('avg', numpy.mean, axis = 0)
statsFit.register('std', numpy.std, axis = 0)
statsFit.register('min', numpy.min, axis = 0)
statsFit.register('max', numpy.max, axis = 0)
