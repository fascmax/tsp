#!/usr/bin/env python
# coding: utf-8

# Representacion de organismos:
# Tupla donde el i-esimo valor representa la i-esima ciudad a visitar


import random
import itertools
import statistics
import math


NUMBER_OF_CITIES = 100
BASE_ORGANISM = [i for i in range(NUMBER_OF_CITIES)]


# Calculo de dominancia de vectores objetivo
def dominant(a, b): return (a[0] <= b[0] and a[1] < b[1]) or (a[0] < b[0] and a[1] <= b[1])

def covers(a, b): return a[0] <= b[0] and a[1] <= b[1]

def init_generation(n):
    return [tuple(random.sample(BASE_ORGANISM, len(BASE_ORGANISM))) for _ in range(n)]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def cluster_distance(c1, c2, f):
    return statistics.mean(distance(f(a),f(b)) for a,b in itertools.product(list(c1), list(c2)))

def get_centroid(cluster, f):
    
    if len(cluster) == 1: return cluster.pop()
    centroid = None
    minDist = None
    for element in cluster:
        dist = sum(distance(f(element), f(e)) for e in cluster if e != element)
        if minDist is None or dist < minDist:
            minDist = dist
            centroid = element
            
    return centroid

def rank_population(population, pareto_set):
    options = []
    scores = []
    strengths = dict()
    for individual in pareto_set:
        options.append(individual)
        strength = sum(1 if covers(individual, i) else 0 for i in population) / (len(population) + 1)
        scores.append(strength)
        strengths[individual] = strength
    
    for individual in population:
        options.append(individual)
        scores.append(sum( strengths[i] if covers(i, individual) else 0 for i in pareto_set) + 1)
    
    return options, scores
def mate(organism1, organism2):
    organism1 = list(organism1)
    organism2 = list(organism2)
    
    cut_point_1 = random.randint(0, len(organism1))
    cut_point_2 = random.randint(0, len(organism1))
    
    if cut_point_1 > cut_point_2: cut_point_1, cut_point_2 = [cut_point_2, cut_point_1]
    
    section = organism1[cut_point_1 : cut_point_2]
    offspring1 = [0] * len(organism1)
    j = 0
    
    for i in range(len(offspring1)):
        if i < cut_point_1:
            while organism2[j] in section: j += 1
            offspring1[i] = organism2[j]
            j += 1
        elif i >= cut_point_1 and i < cut_point_2:
            offspring1[i] = organism1[i]
        elif i >= cut_point_2:
            while organism2[j] in section: j += 1
            offspring1[i] = organism2[j]
            j += 1

    return tuple(offspring1)

def mutate(individual):
    index1, index2 = random.choices(BASE_ORGANISM, k=2)
    mutated_individual = list(individual)
    mutated_individual[index1],mutated_individual[index2] = mutated_individual[index2], mutated_individual[index1]
    
    return tuple(mutated_individual)

def spea(n, iterations, f, P=0.6, MAX_PARETO_SIZE = 50, MUTATION_RATE = 0.1):
    """
    Funcion que ejecuta el algoritmo de SPEA.

    Params:

    * n: tamaño de la poblacion
    * iterations: numero de iteraciones que realizara el algoritmo
    * f: funcion de evaluacion de organismos
    * P: probabilidad de elegir 
    """
            
    def gen_non_dominated_solutions(population, pareto_set, f):
        lista = population + list(pareto_set)
        nuevo = [organism for organism in lista if all(not dominant(f(org), f(organism)) for org in lista)]
        return nuevo

    def cluster_pareto_set(pareto_set, f):
        cluster_set = set((organism, ) for organism in pareto_set)
        
        while len(cluster_set) > MAX_PARETO_SIZE:
            
            min_distance = None
            cluster_1 = None
            cluster_2 = None
            for x, y in itertools.product(list(cluster_set), repeat=2):
                if x == y: continue
                distance = cluster_distance(x, y, f)
                if min_distance is None or distance < min_distance:
                    cluster_1 = set(x)
                    cluster_2 = set(y)
                    min_distance = distance
            new_cluster = list(cluster_1.union(cluster_2))
            new_cluster.sort()
            try:
                cluster_1 = list(cluster_1)
                cluster_1.sort()
                cluster_set.remove(tuple(cluster_1))

                cluster_2 = list(cluster_2)
                cluster_2.sort()
                cluster_set.remove(tuple(cluster_2))
            except:
                print("cluster_Set",cluster_set)
                print("cluster_1",cluster_1)
                print("cluster_2",cluster_2)
                input()
            cluster_set.add(tuple(new_cluster))
            
        
        return set(get_centroid(list(cluster)) for cluster in cluster_set)


    def crossover_population(options, scores):
        weight_sum = sum(scores)
        scores = [weight_sum - s for s in scores]
        new_gen = set()
        while len(new_gen) < len(options):
            parent1 = None
            parent2 = None
            organism1, organism2 = random.sample(range(len(options)), 2)
            if scores[organism1] < scores[organism2]:
                organism1, organism2 = organism2, organism1
            
            if random.random() < P: 
                parent1 = options[organism1]
            else: 
                parent1 = options[organism2]
                
            organism1, organism2 = random.sample(range(len(options)), 2)
            if scores[organism1] < scores[organism2]:
                organism1, organism2 = organism2, organism1
            
            if random.random() < P: 
                parent2 = options[organism1]
            else: 
                parent2 = options[organism2]
            new_gen.add(mate(parent1, parent2))
            
        return list(new_gen)

    def mutate_individuals(new_generation):
        return [mutate(individual) if random.random() < MUTATION_RATE else individual for individual in new_generation ]

    def generate_generation(population, pareto_set):
        options, scores = rank_population(population, pareto_set)
        
        new_generation = crossover_population(options, scores)
        
        return mutate_individuals(new_generation)

    def run_generation(generacion, pareto_set, f):
        
        non_dominated = gen_non_dominated_solutions(generacion, pareto_set, f)
        pareto_set = set(non_dominated)
        
        if len(pareto_set) > MAX_PARETO_SIZE:
            pareto_set = cluster_pareto_set(pareto_set, f)
        generacion = generate_generation(generacion, pareto_set)
        
        return generacion, pareto_set


    # Inicio de algoritmo
    generation = init_generation(n)
    pareto_set = set()
    for _ in range(iterations):
        generation, pareto_set = run_generation(generation, pareto_set, f)
        
    return pareto_set


































