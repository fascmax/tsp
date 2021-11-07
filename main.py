from spea.SPEA import spea
from lector import Y_TRUE_KROAB, mab1, mab2,mac1, mac2, spea_f_builder, Y_TRUE_KROAC
import matplotlib.pyplot as plt
from mas.MAS import calcular_metricas
import math
def run_spea(f, generacion, poblacion):
    pareto_set = spea(poblacion, generacion, f)
    return [{"f1": org[0],"f2": org[1]} for org in map(f, pareto_set)]

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
        run_spea(f, generacion, poblacion)

    elif option == 2:
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Iteraciones del MAS...")))
        K = int((input("Numero de veces que se ejecutara el algoritmo...")))
        (m1,m2,m3,error) = calcular_metricas(m,N,'tsp_KROAB100.TSP.TXT',Y_TRUE_KROAB)
        print(f"{m1=}")
        print(f"{m2=}")
        print(f"{m3=}")
        print(f"{error=}")
    elif option == 3:
        generacion = int((input("Ingrese el número de generaciones para el SPEA...")))
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de iteraciones del MAS...")))
    elif option == 4:
        generacion = int((input("Ingrese el número de generaciones...")))
        poblacion = int((input("Ingrese el tamaño de la poblacion...")))
        f = spea_f_builder(mac1, mac2)        
        run_spea(f, generacion, poblacion)
    elif option == 5:
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Iteraciones del MAS...")))
        K = int((input("Numero de veces que se ejecutara el algoritmo...")))
        (m1,m2,m3,error) = calcular_metricas(m,N,'tsp_kroac100.tsp.txt',Y_TRUE_KROAC ,K,sigma_ac)
        print(f"{m1=}")
        print(f"{m2=}")
        print(f"{m3=}")
        print(f"{error=}")
    elif option == 6:
        generacion = int((input("Ingrese el número de generaciones para el SPEA...")))
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de iteraciones para el MAS...")))



sigma_ac = get_sigma(Y_TRUE_KROAC)

menuPrincipal()