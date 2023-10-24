


'''--------------------++++++++++++++++------------------------------------------------------------+++------------------------------------------------------'''
# geneticAlgorithmPlot(population=cityList,popSize=100,eliteSize=20,mutationRate=0.01,generations=500)


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
cityList=[City(i[0],i[1]) for i in read_tsp_file('lin318.tsp')]

best_route=geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
print(''' \n\nThe initial cities are {} \n ------------------------------++++++++++++--------------------------------------------+++++++++++----------------------------------------\n  
      and best route is {}'''.format(cityList,best_route))



'''-------------------~~~~~~~~~~~~~~~~~~~~~---------------------------------------------------------*********************-----------------------------------'''
# Function to run the TSP-GA and return fitness and objective values
def run_tsp_ga(cityList, popSize, eliteSize, mutationRate, generations, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
        np.random.seed(random_seed)

    fitness_values = []
    objective_values = []

    # Initial population
    pop = initialPopulation(popSize, cityList)
    for i in range(generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        # Calculate fitness and objective values for the best route in this generation
        bestRoute = rankRoutes(pop)[0][0]
        fitness_values.append(Fitness(pop[bestRoute]).routeFitness())
        objective_values.append(Fitness(pop[bestRoute]).routeDistance())

    return fitness_values, objective_values

# Number of runs, generations, and population size
num_runs = 30
generations = 500
popSize = 100

# Lists to store fitness and objective values
avg_fitness_values = []
max_fitness_values = []
avg_objective_values = []
max_objective_values = []

# Run the TSP-GA multiple times with different random seeds
for run in range(num_runs):
    random_seed = random.randint(1, 1000)  # Use a different seed for each run
    fitness_values, objective_values = run_tsp_ga(cityList, popSize, eliteSize=20, mutationRate=0.01, generations=generations, random_seed=random_seed)
    avg_fitness_values.append(np.mean(fitness_values))
    max_fitness_values.append(max(fitness_values))
    avg_objective_values.append(np.mean(objective_values))
    max_objective_values.append(min(objective_values))

# Plot fitness graphs
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(avg_fitness_values, label='Average Fitness')
plt.plot(max_fitness_values, label='Max Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()

# Plot objective values (tour length)
plt.subplot(1, 2, 2)
plt.plot(avg_objective_values, label='Average Objective')
plt.plot(max_objective_values, label='Min Objective')
plt.xlabel('Generation')
plt.ylabel('Objective (Tour Length)')
plt.legend()

plt.tight_layout()
plt.show()
