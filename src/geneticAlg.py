from functools import reduce
from operator import add
from collections import Counter
from deap import creator, base, tools, algorithms

from data import data

smallData = data['nrp3']
customers = smallData['customers']

def getValue(requirement = -1, customer = { 'weight': 0, 'requirements': [] }):
	''' Returns a value between 0 and 1 '''
	requirements = customer['requirements']

	if requirement in requirements:
		length = len(requirements)
		
		return (length - requirements.index(requirement)) / length
	
	return 0
