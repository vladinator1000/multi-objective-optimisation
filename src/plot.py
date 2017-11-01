from pandas import DataFrame
import seaborn
from deap import tools
from matplotlib import pyplot
from pprint import pprint

from toolboxes import nsgaToolbox, singleObjToolbox
from algorithms import runGA, runRandom

# Make a plot figure
fig = pyplot.figure()
ax = fig.gca()
plot_colors = seaborn.color_palette("Set1", n_colors=20)

# Run the random algorithm
randomGenerations, fitnessesPerGen = runRandom()
randomScores = []
randomCosts = []

# Plot results
for gen in fitnessesPerGen:
	for fitness in gen:
		randomScores.append(fitness[0])
		randomCosts.append(fitness[1])

fig, ax = pyplot.subplots()
pyplot.scatter(randomScores, randomCosts, label = 'random', s = 1, color = plot_colors[19], ax = ax)


#
# # Run NSGA2
# for index in range(3):
result, logbook = runGA(nsgaToolbox, maxGen = 10)

fronts = tools.emo.sortLogNondominated(
	result,
	len(result)
)

# Plot genetic results
# for i, individuals in enumerate(fronts):
par = [nsgaToolbox.evaluate(ind) for ind in fronts[0]]
df = DataFrame(par)

# seaborn.kdeplot(df.loc[:, 0], df.loc[:, 1], ax = ax)
# df.plot(
# 	ax = ax,
# 	label = 'Front Gen {}'.format(index),
# 	s = 2,
# 	kind = 'scatter',
# 	x = df.columns[0],
# 	y = df.columns[1],
# 	color = plot_colors[index]
# )



pyplot.xlabel('Score')
pyplot.ylabel('Cost')
pyplot.legend()
pyplot.show()
