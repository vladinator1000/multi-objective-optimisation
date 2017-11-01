from pandas import DataFrame
from seaborn import color_palette
from matplotlib import pyplot, animation
from deap import tools
from pprint import pprint

from toolboxes import nsgaToolbox, statsFit
from algorithms import runGA


# Runs the Genetic Algorithm and animates fronts for each generation
finalGen, logbook = runGA(nsgaToolbox, maxGen = 100)

allGens = logbook.select('allGenerations')

# Calculate fitness stats
allGenerationsFit = []
for generation in allGens:
	allGenerationsFit.append(
		list(
			map(nsgaToolbox.evaluate, generation)
		)
	)

fitnessStats = statsFit.compile(allGenerationsFit)

minimums = fitnessStats['min']
maximums = fitnessStats['max']

minScore = minimums[0][0]
maxScore = maximums[len(maximums) - 1][0]

minCost = minimums[0][1]
maxCost = maximums[len(maximums) - 1][1]

plot_colors = color_palette("Set1", n_colors = 15)

def animate(frame_index, logbook):
	ax.clear()
	ax.set_autoscaley_on(False)
	ax.set_ylim([minCost, maxCost])
	ax.set_xlim([minScore, maxScore])

	allGenerations = logbook.select('allGenerations')

	fronts = tools.emo.sortLogNondominated(
		allGenerations[frame_index],
		len(allGenerations[frame_index])
	)

	for i, individuals in enumerate(fronts):
		par = [nsgaToolbox.evaluate(ind) for ind in individuals]
		dataFrame = DataFrame(par)

		dataFrame.plot(
			ax = ax,
			kind = 'scatter',
			label = 'Front ' + str(i + 1),
			x = dataFrame.columns[0],
			y = dataFrame.columns[1],
			color = plot_colors[i]
		)

	ax.set_title('Generation: ' + str(frame_index))
	ax.set_xlabel('Score (trying to maximise)')
	ax.set_ylabel('Cost (trying to minimise)')

	return []

fig = pyplot.figure()
ax = fig.gca()

anim = animation.FuncAnimation(
	fig,
	lambda i: animate(i, logbook),
	frames=len(logbook),
	interval=1,
	blit=True
)

pyplot.show()
