import random

def apply_mutation(chromosome, mutation_probability=0.1):
    for index in range(len(chromosome)):
        if random.random() < mutation_probability:
            chromosome[index] = 1 - chromosome[index]
    return chromosome

base_solution = [1, 1, 1, 1, 1]
mutated_solution = apply_mutation(base_solution)