import math
#@author Francisco Candia
def distance(o1,o2):
    return int(abs(o1-o2))
def m2(pareto_set,sigma):
    cardinality = len(pareto_set)
    total_wp = 0
    for solucion1 in pareto_set:
        wp_count = 0
        for solucion2 in pareto_set:
            if euclidean_distance(solucion1,solucion2) > sigma:
                wp_count +=1
        total_wp += wp_count
    return total_wp/(cardinality-1)
def m3(pareto_set):
    max_distance = 0
    total = 0 
    for solucion1 in pareto_set:
        for solucion2 in pareto_set:
            if distance(solucion1['f1'],solucion2['f1']) > max_distance:
                max_distance = distance(solucion1['f1'],solucion2['f1'])
    total += max_distance
    max_distance = 0
    for solucion1 in pareto_set:
        for solucion2 in pareto_set:
            if distance(solucion1['f2'],solucion2['f2']) > max_distance:
                max_distance = distance(solucion1['f2'],solucion2['f2'])
    return math.sqrt(total)
def euclidean_distance(a,b):
    return math.sqrt((a['f1']-b['f1'])**2 + (a['f2']-b['f2'])**2) 
def m1(pareto_front, true_front):
    cardinality = len(pareto_front)
    count = 1/cardinality
    total = 0 
    min_distance = math.inf
    for solucion1 in pareto_front:
        min_distance = math.inf
        for solucion2 in true_front:
            if euclidean_distance(solucion1,solucion2) < min_distance:
                min_distance = euclidean_distance(solucion1,solucion2)
        total += min_distance
    return count * total
def error(pareto_front, true_front):
    cardinality = len(pareto_front)
    count = 0
    for solucion in pareto_front:
        if solucion in true_front:
            count = count + 1
    return 1-count/cardinality