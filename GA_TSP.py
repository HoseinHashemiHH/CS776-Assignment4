


'''--------------------++++++++++++++++------------------------------------------------------------+++------------------------------------------------------'''

from methodes import initialPopulation,createRoute,rankRoutes
from goToNextGeneration import nextGeneration
from plot import geneticAlgorithmPlot
import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from City import City
from FItness import Fitness
from selection import selection
from xover import *
from flip import mutate,mutatePopulation
from tsp_reader import read_tsp_file


'''--------------------------------------------------------------------+++++++++++++++++++++++-------------------------------------------------------------'''
def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute
'''------------------------------------------+++++++++++++---------------------------++++++++++++----------------------------------------------------------'''
# cityList = []

# for i in range(0,25):
#     cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
cityList=[City(i[0],i[1]) for i in read_tsp_file('burma14.tsp')]

best_route=geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
print(''' \n\nThe initial cities are {} \n ------------------------------++++++++++++--------------------------------------------+++++++++++----------------------------------------\n  
      and best route is {}'''.format(cityList,best_route))

# geneticAlgorithmPlot(population=cityList,popSize=100,eliteSize=20,mutationRate=0.01,generations=500)

