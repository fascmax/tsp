from spea.spea import spea
from lector import mab1, mab2,mac1, mac2, spea_f_builder

def run_spea(f, generacion, poblacion):
    pareto_set = spea(poblacion, generacion, f)
    return [{"f1": org[0],"f2": org[1]} for org in map(f, pareto_set)]


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
        N = int((input("Ingrese el número de Iteraciones...")))
    elif option == 3:
        generacion = int((input("Ingrese el número de generaciones para el SPEA...")))
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de iteraciones para el MAS...")))
    elif option == 4:
        generacion = int((input("Ingrese el número de generaciones...")))
        poblacion = int((input("Ingrese el tamaño de la poblacion...")))
        f = spea_f_builder(mac1, mac2)        
        run_spea(f, generacion, poblacion)
    elif option == 5:
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de Iteraciones...")))
    elif option == 6:
        generacion = int((input("Ingrese el número de generaciones para el SPEA...")))
        m = int((input("Ingrese el número de hormigas...")))
        N = int((input("Ingrese el número de iteraciones para el MAS...")))



menuPrincipal()