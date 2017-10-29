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

# 
'''
	Data in the form of:
	dict = {
		textFileName: {
			requirementCosts: number[],
			customers: [
				{ weight: float, requirements: number[] },
				...
			]
		}
	}
'''
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
	requirementCosts = rows[1:numLevels * 2 + 1]

	# Flatten [[1], [2, 3], ...] to [1, 2, 3, ...]
	requirementCosts = list(chain(*requirementCosts[1::2]))


	withoutRequirementCosts = rows[numLevels * 2 + 1:]
	rowsToSkip = withoutRequirementCosts[0][0]

	customerRows = withoutRequirementCosts[rowsToSkip + 2:]

	fileName = basename(path).strip('.txt')

	data[fileName] = {
		'requirementCosts': requirementCosts[:],
		'customers': [],
	}

	for row in customerRows:
		profit = row[0]

		data[fileName]['customers'].append({
			'weight': profit / len(customerRows),
			'requirements': row[2:]
		})

print('Data loaded.') 
