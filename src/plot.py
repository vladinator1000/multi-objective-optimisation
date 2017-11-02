from pandas import DataFrame
import seaborn
from deap import tools
from matplotlib import pyplot as plt
from pprint import pprint
from itertools import chain

from toolboxes import nsgaToolbox, singleObjToolbox
from algorithms import runGA, runRandom

ITERATIONS = 10
GENERATIONS = 200

# Make a plot figure
fig, ax = plt.subplots()
plot_colors = seaborn.color_palette("Set1", n_colors=20)


randomScores = []
randomCosts = []
fronts = []
singleObjHallOfFame = tools.HallOfFame(GENERATIONS * ITERATIONS)

for i in range(ITERATIONS):
	# Run the random algorithm
	randomGenerations, fitnessesPerGen = runRandom(maxGen = GENERATIONS)

	for gen in fitnessesPerGen:
		for fitness in gen:
			randomScores.append(fitness[0])
			randomCosts.append(fitness[1])

	# Run single objective
	singleResult, singleLogbook = runGA(
		singleObjToolbox,
		maxGen = GENERATIONS,
		hallOfFame = singleObjHallOfFame
	)

	# Run NSGA2
	nsgaResult, nsgaLogbook = runGA(nsgaToolbox, maxGen = GENERATIONS)

	front = tools.emo.sortLogNondominated(
		nsgaResult,
		len(nsgaResult),
		first_front_only = True
	)

	# Fitness for every front
	fronts.append(list(nsgaToolbox.evaluate(ind) for ind in front))


# Plot results from random
seaborn.kdeplot(
	randomScores,
	randomCosts,
	ax = ax,
	cmap = 'Blues',
)

plt.scatter(
	randomScores,
	randomCosts,
	label = '(blue) Random',
	s = 3,
	color = 'b',
	alpha = .5 / ITERATIONS
)

# Plot fronts from NSGA2
flatNsgaFronts = list(chain(*fronts))
nsgaDf = DataFrame(flatNsgaFronts)

seaborn.kdeplot(
	nsgaDf[nsgaDf.columns[0]],
	nsgaDf[nsgaDf.columns[1]],
	ax = ax,
	cmap = 'Reds',
)

plt.scatter(
	nsgaDf[nsgaDf.columns[0]],
	nsgaDf[nsgaDf.columns[1]],
	label = '(red) NSGA2 Last Fronts For {} Iters'.format(ITERATIONS),
	s = 3,
	color = 'r',
	alpha = .3
)

# Get score and cost of single obj
singleFits = list(map(nsgaToolbox.evaluate, singleObjHallOfFame))
singleFitsDf = DataFrame(singleFits)
print(singleFits)

# Plot single objective
seaborn.kdeplot(
	singleFitsDf[singleFitsDf.columns[0]],
	singleFitsDf[singleFitsDf.columns[1]],
	ax = ax,
	cmap = 'Greens',
)

plt.scatter(
	singleFitsDf[singleFitsDf.columns[0]],
	singleFitsDf[singleFitsDf.columns[1]],
	label = '(green) Single Objective Hall Of Fame',
	s = 3,
	color = 'g',
	alpha = 1.0 / ITERATIONS
)

plt.xlabel('Score')
plt.ylabel('Cost')
plt.title('Results for {} iterations, {} generations each.'.format(ITERATIONS, GENERATIONS))
plt.legend()
plt.show()
