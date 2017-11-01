from pandas import DataFrame
from seaborn import color_palette
from matplotlib import pyplot, animation
from deap import tools

from algorithms import toolbox, runGA


# Runs the Genetic Algorithm and animates fronts for each generation
result, logbook = runGA(toolbox, maxGen = 100)

plot_colors = color_palette("Set1", n_colors=20)

def animate(frame_index, logbook):
	ax.clear()
	ax.set_autoscaley_on(False)
	ax.set_ylim([5000, 5500])
	ax.set_xlim([2, 3])
	fronts = tools.emo.sortLogNondominated(
		logbook.select('populaton')[frame_index],
		len(logbook.select('populaton')[frame_index])
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


anim = animation.FuncAnimation(
	fig,
	lambda i: animate(i, logbook),
	frames=len(logbook),
	interval=1,
	blit=True
)

pyplot.show()
