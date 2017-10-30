from deap import algorithms, base, benchmarks, tools, creator
from random import randint
from numpy import dot
from matplotlib import pyplot, animation
from copy import deepcopy
from pandas import DataFrame
from seaborn import color_palette

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
toolbox.pop_size = 10
toolbox.max_gen = 10
toolbox.mut_prob = 0.1

def runGA(toolbox, stats = None, verbose = False):
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


# Store individuals in logbook
stats = tools.Statistics()
stats.register("pop", deepcopy)

# Run the algorithm
result, logbook = runGA(toolbox, stats = stats)


plot_colors = color_palette("Set1", n_colors=20)

def animate(frame_index, logbook):
	ax.clear()
	fronts = tools.emo.sortLogNondominated(
		logbook.select('pop')[frame_index], 
		len(logbook.select('pop')[frame_index])
	)

	for i, individuals in enumerate(fronts):
		par = [toolbox.evaluate(ind) for ind in individuals]
		dataFrame = DataFrame(par)

		dataFrame.plot(
			ax = ax,
			kind = 'scatter',
			label = 'Front ' + str(i + 1), 
			x = dataFrame.columns[0],
			y = dataFrame.columns[1], 
			color=plot_colors[i]
		)
		
	ax.set_title('Generation: ' + str(frame_index))
	ax.set_xlabel('Score (trying to maximise)')
	ax.set_ylabel('Cost (trying to minimise)')
	
	return []

fig = pyplot.figure()
ax = fig.gca()

anim = animation.FuncAnimation(fig, lambda i: animate(i, logbook), 
	frames=len(logbook),
	interval=15, 
	blit=True
)

pyplot.show()