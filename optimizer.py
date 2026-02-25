import numpy as np
import random
import networkx as nx

class GeneticRouteOptimizer:
    def __init__(self, graph, nodes, locations, pop_size=100, generations=200):
        self.G = graph
        self.nodes = nodes
        self.locations = locations # list of node IDs [origin, d1, d2...]
        self.pop_size = pop_size
        self.generations = generations
        self.dist_matrix = self._build_dist_matrix()

    def _build_dist_matrix(self):
        """Precompute shortest paths between all selected points (M.Tech optimization)"""
        size = len(self.locations)
        matrix = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                if i == j: continue
                try:
                    matrix[i][j] = nx.shortest_path_length(
                        self.G, self.locations[i], self.locations[j], weight='weight'
                    )
                except nx.NetworkXNoPath:
                    matrix[i][j] = 1e9 # Penalty for unreachable nodes
        return matrix

    def _get_fitness(self, genome):
        """Total path distance; lower is better."""
        # Genome is a permutation of indices 1 to N (excluding origin at index 0)
        dist = self.dist_matrix[0][genome[0]] # Origin to first dest
        for i in range(len(genome) - 1):
            dist += self.dist_matrix[genome[i]][genome[i+1]]
        return dist

    def solve(self):
        n_dest = len(self.locations) - 1
        indices = list(range(1, n_dest + 1))
        
        # Initialize population
        population = [random.sample(indices, n_dest) for _ in range(self.pop_size)]

        for _ in range(self.generations):
            # Sort by fitness
            population = sorted(population, key=lambda g: self._get_fitness(g))
            
            # Elitism: Keep top 10%
            next_gen = population[:int(self.pop_size * 0.1)]

            # Crossover & Mutation
            while len(next_gen) < self.pop_size:
                parent1, parent2 = random.sample(population[:50], 2)
                # Ordered Crossover (OX) for TSP
                child = self._ordered_crossover(parent1, parent2)
                # Swap Mutation
                if random.random() < 0.2:
                    idx1, idx2 = random.sample(range(n_dest), 2)
                    child[idx1], child[idx2] = child[idx2], child[idx1]
                next_gen.append(child)
            population = next_gen

        best_genome = population[0]
        return [0] + best_genome # Return full index path

    def _ordered_crossover(self, p1, p2):
        size = len(p1)
        a, b = sorted(random.sample(range(size), 2))
        child = [None] * size
        child[a:b] = p1[a:b]
        p2_remaining = [item for item in p2 if item not in child]
        ptr = 0
        for i in range(size):
            if child[i] is None:
                child[i] = p2_remaining[ptr]
                ptr += 1
        return child