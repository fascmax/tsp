import random
import matplotlib.pyplot as plt
from lector import leer_txt,cargar_matriz
#Hiperparametros
m = 10 #El profe puso 10
k_prima = 10 #El profe puso 500
rho = 0.1
lamb = 0.8
N = 1000
feromona_inicial = 100
beta = 2

#Instancia de TSP
n = 100

#Parametros
feromonas = {}
conjunto_pareto = []


MAX_VALUE1 = 0
MAX_VALUE2 = 0

def iniciacilizar_parametros():
    global feromonas
    global conjunto_pareto 
    feromonas = {}
    conjunto_pareto = []



def get_feromona(i,j):
    if i > j:
        aux = i
        i = j
        j = aux
    if (i,j) in feromonas:
        return feromonas[(i,j)]
    return feromona_inicial

def actualizar_feromonas(solucion):
    delta_tau = 1 / (solucion['f1']/MAX_VALUE1 + solucion['f2']/MAX_VALUE2) #4.6
    for arista in solucion['aristas']:
        feromona = get_feromona(arista[0],arista[1]) #arista tiene la forma (i,j)
        feromona = (1-rho)*feromona + rho*delta_tau #4.4
        feromonas[arista] = feromona



def reiniciar_feromonas():
    global feromonas
    feromonas = {}



def condicion_parada(generacion):
    #Se detiene cuando es mayor o igual a N
    return generacion >= N





def get_visibilidad(i,j,objetivo):
    if objetivo == 1:
        return 1/costos1[i][j]
    elif objetivo == 2:
        return 1/costos2[i][j]
    
            





def calcular_probabilidad_numerador(i,j,lambda_k):
    tau = get_feromona(i,j)
    eta1 = get_visibilidad(i,j,1)
    eta2 = get_visibilidad(i,j,2)
    return tau * (eta1 ** (lambda_k*beta)) * (eta2 ** ((1-lambda_k)*beta)) 





def calcular_probabilidad_denominador(i,vecindario,lambda_k):
    suma = 0
    for x in vecindario:
        tau = get_feromona(i,x)
        eta1 = get_visibilidad(i,x,1)
        eta2 = get_visibilidad(i,x,2)
        suma += tau * (eta1 ** (lambda_k*beta)) * (eta2 ** ((1-lambda_k)*beta)) 
    if suma == 0:
        return 1
    return suma 





def siguiente_nodo(i,vecindario,lambda_k):
    denominador = calcular_probabilidad_denominador(i,vecindario,lambda_k) 
    probabilidades = [calcular_probabilidad_numerador(i,j,lambda_k)/denominador for j in vecindario]
    return random.choices(vecindario,weights=probabilidades)[0]





def construir_solucion(lambda_k):
    solucion = {"aristas": [], "f1": 0, "f2": 0}
    vecindario = set(range(n))
    inicial = random.randint(0,99)
    actual = inicial
    vecindario.remove(inicial)
    while len(vecindario) != 0:
        siguiente = siguiente_nodo(actual,list(vecindario),lambda_k)
        solucion['aristas'].append((actual,siguiente))
        solucion['f1'] += costos1[actual][siguiente]
        solucion['f2'] += costos2[actual][siguiente]
        actual = siguiente      
        vecindario.remove(actual)
        
    solucion['aristas'].append((actual,inicial))
    solucion['f1'] += costos1[actual][inicial]
    solucion['f2'] += costos2[actual][inicial]
    return solucion





def es_dominado(solucion,solucion_pareto):
    if solucion_pareto['f1'] <= solucion['f1'] and solucion_pareto['f2'] <= solucion['f2']:
        if solucion_pareto['f1'] < solucion['f1'] or solucion_pareto['f2'] < solucion['f2']:
            return True
    return False





def actualizar_conjunto_pareto(solucion):
    global conjunto_pareto
    for solucion_pareto in conjunto_pareto:
        if es_dominado(solucion,solucion_pareto):
            return False
    nuevo_conjunto_pareto = []
    for solucion_pareto in conjunto_pareto:
        if not es_dominado(solucion_pareto,solucion):
            nuevo_conjunto_pareto.append(solucion_pareto)
    conjunto_pareto = nuevo_conjunto_pareto
    conjunto_pareto.append(solucion)
    return True






def MAS():
    generacion = 0
    desde_sin_cambio = 0
    iniciacilizar_parametros()
    while not condicion_parada(generacion):
        generacion = generacion  + 1
        se_actualizo = False
        for i in range(m):
            solucion = construir_solucion(i) # Ecuacion 4.9
            bandera = actualizar_conjunto_pareto(solucion) 
            se_actualizo = se_actualizo or bandera
            if bandera:
                actualizar_feromonas(solucion) # Ecuacion 4.2
        if se_actualizo:
            desde_sin_cambio = 0
        else:
            desde_sin_cambio += 1
        if desde_sin_cambio > k_prima:
            reiniciar_feromonas()
   # for solucion in conjunto_pareto:
    #    print(solucion)



#Find max value to normalize
l1 = leer_txt('tsp_KROAB100.TSP.TXT')
costos1, costos2 = cargar_matriz(l1)
for row in costos1:
    for i  in range(len(row)):
        row[i] = float(row[i])
for row in costos2:
    for i  in range(len(row)):
        row[i] = float(row[i])
for row in costos1:
    MAX_VALUE1 += max(row)
for row in costos2:
    MAX_VALUE2 += max(row)

MAS()
plot1 = plt.figure(1)
plt.title('KROAB100')
plt.plot([x['f1'] for x in conjunto_pareto],[y['f2'] for y in conjunto_pareto],'o', color='black')

l1 = leer_txt('tsp_kroac100.tsp.txt')
costos1, costos2 = cargar_matriz(l1)
for row in costos1:
    for i  in range(len(row)):
        row[i] = float(row[i])
for row in costos2:
    for i  in range(len(row)):
        row[i] = float(row[i])
MAX_VALUE1 = 0
MAX_VALUE2 = 0
for row in costos1:
    MAX_VALUE1 += max(row)
for row in costos2:
    MAX_VALUE2 += max(row)
conjunto_pareto=[]
MAS()
plot2 = plt.figure(2)
plt.plot([x['f1'] for x in conjunto_pareto],[y['f2'] for y in conjunto_pareto],'o', color='black')
plt.title('KROAC100')
plt.show()
