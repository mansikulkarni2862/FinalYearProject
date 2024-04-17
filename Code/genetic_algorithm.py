import random

class GeneticAlgorithm:
    def __init__(self, chromosome_length, population_size, fitness_function, crossover_rate=0.8, mutation_rate=0.1):
        self.chromosome_length = chromosome_length
        self.population_size = population_size
        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def create_chromosome(self):
        return [random.random() for _ in range(self.chromosome_length)]

    def create_population(self):
        return [self.create_chromosome() for _ in range(self.population_size)]

    def selection(self, population):
        population_with_fitness = [(chromosome, self.fitness_function(chromosome)) for chromosome in population]
        population_with_fitness.sort(key=lambda x: x[1], reverse=True)
        selected_parents = [chromosome for chromosome, _ in population_with_fitness[:self.population_size // 2]]
        return selected_parents

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.chromosome_length - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        else:
            return parent1, parent2

    def mutation(self, chromosome):
        if random.random() < self.mutation_rate:
            mutation_point = random.randint(0, self.chromosome_length - 1)
            chromosome[mutation_point] = random.random()
        return chromosome

    def evolve(self, population):
        selected_parents = self.selection(population)
        next_generation = []
        while len(next_generation) < self.population_size:
            parent1 = random.choice(selected_parents)
            parent2 = random.choice(selected_parents)
            child1, child2 = self.crossover(parent1, parent2)
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)
            next_generation.append(child1)
            next_generation.append(child2)
        return next_generation
