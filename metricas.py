import math
def distance(o1,o2):
    return int(abs(o1-o2))
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