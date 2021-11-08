from spea.SPEA import spea
from lector import Y_TRUE_KROAB, mab1, mab2,mac1, mac2, spea_f_builder, Y_TRUE_KROAC
import matplotlib.pyplot as plt
from mas.MAS import calcular_metricas
from metricas import m1,m2,m3,error
import math
def run_spea(f, generacion, poblacion,simulaciones,y_true):
    M1 = 0
    M2 = 0
    M3 = 0
    ERROR = 0
    for i in range(simulaciones):
        pareto_set = spea(poblacion, generacion, f)
        pareto_set = [{"f1": org[0],"f2": org[1]} for org in map(f, pareto_set)]
        M1 += m1(pareto_set,y_true)
        M2 += m2(pareto_set,sigma_ac)
        M3 += m3(pareto_set)
        ERROR += error(pareto_set,y_true)
    M1 /= simulaciones
    M2 /= simulaciones
    M3 /= simulaciones
    ERROR /= simulaciones
    return M1,M2,M3,ERROR,pareto_set

def get_sigma(y_true):
    lowest_1 = y_true[0]
    lowest_2 = y_true[1]
    for solucion in y_true:
        if solucion['f1'] < lowest_1['f1']:
            lowest_1 = solucion
    for solucion in y_true:
        if solucion['f2'] < lowest_2['f2']:
            lowest_2 = solucion
    return math.sqrt((lowest_1['f1'] - lowest_2['f1'])**2 + (lowest_1['f2']-lowest_2['f2'])**2)/10


def menuPrincipal():
    print('1. KROAB100. SPEA')
    print('2. KROAB100. MAS')
    print('3. KROAB100. SPEA vs MAS')
    print('4. KROAC100. SPEA')
    print('5. KROAC100. MAS')
    print('6. KROAC100. SPEA vs MAS')

    option = int(input("Ingrese una opción..."))
    while not option in [1,2,3,4,5,6]:
        option = int(input("Ingrese una opción..."))
    if option == 1:
        generacion = int((input("Ingrese el número de generaciones...")))
        poblacion = int((input("Ingrese el tamaño de la poblacion...")))
        f = spea_f_builder(mab1, mab2)        
        (M1,M2,M3,ERROR,pareto) = run_spea(f, generacion, poblacion,10,Y_TRUE_KROAB)
        print(f"{M1=}")
        print(f"{M2=}")
        print(f"{M3=}")
        print(f"{ERROR=}")
    elif option == 2:
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Iteraciones del MAS...")))
        K = int((input("Numero de veces que se ejecutara el algoritmo...")))
        (M1,M2,M3,ERROR) = calcular_metricas(m,N,'./datasets/tsp_kroab100.tsp.txt',Y_TRUE_KROAB,K,sigma_ab)
        print(f"{M1=}")
        print(f"{M2=}")
        print(f"{M3=}")
        print(f"{ERROR=}")
    elif option == 3:
        generacion = int((input("Ingrese el número de generaciones para el SPEA...")))
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de iteraciones del MAS...")))
    elif option == 4:
        generacion = int((input("Ingrese el número de generaciones...")))
        poblacion = int((input("Ingrese el tamaño de la poblacion...")))
        f = spea_f_builder(mac1, mac2)        
        (M1,M2,M3,ERROR,pareto) = run_spea(f, generacion, poblacion,10,Y_TRUE_KROAC)
        print(f"{M1=}")
        print(f"{M2=}")
        print(f"{M3=}")
        print(f"{ERROR=}")
    elif option == 5:
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Iteraciones del MAS...")))
        K = int((input("Numero de veces que se ejecutara el algoritmo...")))
        (M1,M2,M3,ERROR) = calcular_metricas(m,N,'./datasets/tsp_kroac100.tsp.txt',Y_TRUE_KROAC ,K,sigma_ac)
        print(f"{M1=}")
        print(f"{M2=}")
        print(f"{M3=}")
        print(f"{ERROR=}")
    elif option == 6:
        generacion = int((input("Ingrese el número de generaciones para el SPEA...")))
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de iteraciones para el MAS...")))



sigma_ac = get_sigma(Y_TRUE_KROAC)
sigma_ab = get_sigma(Y_TRUE_KROAB)
menuPrincipal()