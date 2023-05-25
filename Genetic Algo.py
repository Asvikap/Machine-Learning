import random

# Define problem
target = "Hello, World!"
gene_pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,!"

# Define genetic algorithm parameters
population_size = 100
mutation_rate = 0.01
generations = 1000

# Initialize population
def create_individual():
    return [random.choice(gene_pool) for _ in range(len(target))]

population = [create_individual() for _ in range(population_size)]

# Define fitness function
def fitness(individual):
    return sum(1 for expected, actual in zip(target, individual) if expected == actual)

# Genetic algorithm
for generation in range(generations):
    # Evaluate fitness
    fitness_scores = [(individual, fitness(individual)) for individual in population]
    fitness_scores.sort(key=lambda x: x[1], reverse=True)
    print(f"Generation {generation}: {fitness_scores[0][0]} ({fitness_scores[0][1]})")
    # Stop if target is found
    if fitness_scores[0][1] == len(target):
        break
    # Select parents
    parents = [individual for individual, _ in fitness_scores[:10]]
    # Create offspring
    offspring = []
    while len(offspring) < population_size:
        parent1, parent2 = random.choices(parents, k=2)
        child = parent1.copy()
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = random.choice(gene_pool)
        offspring.append(child)
    population = offspring