import os
import csv
import pandas as pd

from itertools import chain
from copy import deepcopy
from ntpath import basename
from pprint import pprint


location = os.path.realpath(
	os.path.join(os.getcwd(), os.path.dirname(__file__))
)

filePaths = [
	os.path.join(location, '../classic-nrp/nrp3.txt'),
	os.path.join(location, '../realistic-nrp/nrp-e3.txt')
]

# Read text files and map them to dicts
data = {}

for path in filePaths:
	rows = []

	for line in open(path):
		split_strings = [string.strip('\n') for string in line.split(' ')]

		# Filter empty strings
		filtered = list(filter(None, split_strings))
		numbers = list(map(int, filtered))
		rows.append(numbers)


	numLevels = rows[0][0]
	requirements = rows[1:numLevels * 2 + 1]

	# Flatten [[1], [2, 3], ...] to [1, 2, 3, ...]
	requirements = list(chain(*requirements[1::2]))


	withoutRequirements = rows[numLevels * 2 + 1:]
	rowsToSkip = withoutRequirements[0][0]

	withoutDeps = withoutRequirements[rowsToSkip + 2:]

	customers = {}
	fileName = basename(path).strip('.txt')

	data[fileName] = {
		'requirements': requirements[:],
		'customers': {},
	}

	for i, row in enumerate(withoutDeps):
		data[fileName]['customers'][i] = {}
		data[fileName]['customers'][i]['profit'] = row[0]
		data[fileName]['customers'][i]['numReqs'] = row[1]
		data[fileName]['customers'][i]['requirements'] = row[2:]

	# Copy stuff to new object


pprint('Data loaded:', data[].keys())
