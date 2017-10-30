from pandas import DataFrame
from seaborn import color_palette
from deap import tools

from algorithms import toolbox, runGA, runRandom

# Make a plot figure
fig = pyplot.figure()
ax = fig.gca()
plot_colors = color_palette("Set1", n_colors=20)

# Run the random algorithm
randomGenerations, fitnessesPerGen = randomAlg()
randomScores = []
randomCosts = []

# Plot results
for gen in fitnessesPerGen:
	for fitness in gen:
		randomScores.append(fitness[0])
		randomCosts.append(fitness[1])

pyplot.scatter(randomScores, randomCosts, label = 'random', s = 2)


# Run the Genetic Algorithm
result, logbook = runGA(toolbox, stats = stats)

fronts = tools.emo.sortLogNondominated(
	logbook.select('pop')[-1],
	len(logbook.select('pop')[-1])
)

# Plot genetic results
for i, individuals in enumerate(fronts):
	par = [toolbox.evaluate(ind) for ind in individuals]
	dataFrame = DataFrame(par)

	dataFrame.plot(
		ax = ax,
		kind = 'scatter',
		label = 'NSGA2 Gen {} Front'.format(len(logbook) - 1),
		x = dataFrame.columns[0],
		y = dataFrame.columns[1],
		color=plot_colors[i]
	)

pyplot.xlabel('Score')
pyplot.ylabel('Cost')
pyplot.legend()
pyplot.show()
