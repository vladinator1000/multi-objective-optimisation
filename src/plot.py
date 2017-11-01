from pandas import DataFrame
from seaborn import color_palette
from deap import tools
from matplotlib import pyplot

from algorithms import toolbox, stats, runGA, runRandom

# Make a plot figure
fig = pyplot.figure()
ax = fig.gca()
plot_colors = color_palette("Set1", n_colors=20)

# Run the random algorithm
randomGenerations, fitnessesPerGen = runRandom()
randomScores = []
randomCosts = []

# Plot results
for gen in fitnessesPerGen:
	for fitness in gen:
		randomScores.append(fitness[0])
		randomCosts.append(fitness[1])

pyplot.scatter(randomScores, randomCosts, label = 'random', s = 2)


# Run NSGA2
result, logbook = runGA(toolbox)

fronts = tools.emo.sortLogNondominated(
	result,
	len(result)
)

# Plot genetic results
for i, individuals in enumerate(fronts):
	par = [toolbox.evaluate(ind) for ind in individuals]
	dataFrame = DataFrame(par)

	dataFrame.plot(
		ax = ax,
		kind = 'scatter',
		label = 'NSGA2 Last Generation Front',
		x = dataFrame.columns[0],
		y = dataFrame.columns[1],
		color = plot_colors[i]
	)

pyplot.xlabel('Score')
pyplot.ylabel('Cost')
pyplot.legend()
# pyplot.show()


print(logbook.select('gen', 'avgScore', 'stdScore'))
