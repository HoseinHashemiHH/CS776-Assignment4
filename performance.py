





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

cityList=[City(i[0],i[1]) for i in read_tsp_file('lin318.tsp')]

best_route=geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
print(''' \n\nThe initial cities are {} \n ------------------------------++++++++++++--------------------------------------------+++++++++++----------------------------------------\n  
      and best route is {}'''.format(cityList,best_route))


# Function to evaluate the TSP-GA's performance
def evaluate_tsp_ga(cityList, popSize, eliteSize, mutationRate, generations, quality_threshold, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
        np.random.seed(random_seed)

    objective_values = []

    # Initial population
    pop = initialPopulation(popSize, cityList)
    for i in range(generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        # Calculate the objective value for the best route in this generation
        bestRoute = rankRoutes(pop)[0][0]
        objective_values.append(Fitness(pop[bestRoute]).routeDistance())

    # Calculate the percentage distance from optimum (if known)
    optimum = known_optimal_solution  # Replace with the known optimum if available
    percentage_distance = [(optimum - value) / optimum * 100 for value in objective_values]

    # Calculate the number of evaluations needed to reach a certain quality level
    num_evaluations_needed = 0
    for value in objective_values:
        num_evaluations_needed += 1
        if (optimum - value) / optimum * 100 <= quality_threshold:
            break

    return percentage_distance, num_evaluations_needed

# Known optimal solution (replace with the actual value if available)
known_optimal_solution = 530000 # Replace with the known optimal solution

# Number of runs, generations, and population size
num_runs = 30
generations = 100
popSize = 100
quality_threshold = 5  # Set the quality threshold (e.g., 5% from optimum)

# Lists to store evaluation results
percentage_distances = []
num_evaluations = []

# Run the TSP-GA multiple times with different random seeds
for run in range(num_runs):
    random_seed = random.randint(1, 1000)  # Use a different seed for each run
    percentage_distance, num_evaluation = evaluate_tsp_ga(cityList, popSize, eliteSize=20, mutationRate=0.01, generations=generations, quality_threshold=quality_threshold, random_seed=random_seed)
    percentage_distances.append(percentage_distance)
    num_evaluations.append(num_evaluation)

# Calculate reliability (percentage of runs within quality)
reliability = sum(1 for dist in percentage_distances if dist[-1] <= quality_threshold) / num_runs * 100

# Calculate average number of evaluations needed to reach quality
avg_num_evaluations = sum(num_evaluations) / num_runs

# Output the results
print('percentage of distance from the optimal value is: ',abs(sum(percentage_distance)/len(percentage_distance)))
print(f"Reliability: {reliability}%")
print(f"Average Number of Evaluations Needed: {avg_num_evaluations}")
