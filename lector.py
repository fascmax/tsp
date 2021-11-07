import pandas as pd

KROAB_FILE = 'datasets/tsp_kroab100.tsp.txt'
Y_TRUE_KROAB_FILE = 'datasets/y_true_kroab100.csv'
KROAC_FILE = 'datasets/tsp_kroac100.tsp.txt'
Y_TRUE_KROAC_FILE = 'datasets/y_true_kroac100.csv'

def leer_txt(archivo):
    lines = []
    with open(archivo, 'r') as f:
        lines = f.readlines()
    return lines

def cargar_matriz(lines):
    mat1 = []
    mat2 = []
    for i in range(100):
        mat1.append([float(val) for val in lines[2+i].split()])
        mat2.append([float(val) for val in lines[103+i].split()])
    return mat1, mat2
    


l1 = leer_txt(KROAB_FILE)
l2 = leer_txt(KROAC_FILE)
mab1, mab2 = cargar_matriz(l1)
mac1, mac2 = cargar_matriz(l2)


def spea_f_builder(matriz_obj_a, matriz_obj_b):
    def f(x):
    
        objetivo_a = 0
        objetivo_b = 0
        curr_city = None
        first_city = None
        for city in x:
            if curr_city is not None:
                objetivo_a += matriz_obj_a[curr_city][city]
                objetivo_b += matriz_obj_b[curr_city][city]
            else:
                first_city = city
            
            curr_city = city
        
        objetivo_a += matriz_obj_a[curr_city][first_city]
        objetivo_b += matriz_obj_b[curr_city][first_city]
        
        return objetivo_a, objetivo_b
    return f
