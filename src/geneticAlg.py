from functools import reduce
from operator import add
from collections import Counter
from deap import creator, base, tools, algorithms

from data import data

def value(requirement = -1, customer = { 'requirements': [] }):
	'''
	How valuable a requirement is to a customer.
	Returns a value between 0 and 1.

	1 for the first requirement, 
	proportionally smaller to customer requirements length thereafter.
	'''

	requirements = customer['requirements']

	if requirement in requirements:
		length = len(requirements)
		
		return (length - requirements.index(requirement)) / length
	
	return 0.0

def score(requirement = -1, customers = [{ 'weight': 0.0, 'requirements': [] }]):
	'''
	The sum of scores of a requirement for each customer.
	'''
	score = 0

	for customer in customers:
		score += customer['weight'] * value(requirement, customer)
	
	return score


def scoreVector(dataSet = { 
	'requirementCosts': [],
	'customers': [{ 'weight': 0.0, 'requirements': [] }]
}):
	numberOfRequirements = len(dataSet['requirementCosts'])

	result = []

	for index in range(numberOfRequirements):
		currentScore = score(index, customers)
		
		result.append(currentScore)

	return result
