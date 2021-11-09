from spea.SPEA import spea
from lector import Y_TRUE_KROAB, mab1, mab2,mac1, mac2, spea_f_builder, Y_TRUE_KROAC
import matplotlib.pyplot as plt
from mas.MAS import calcular_metricas
from metricas import m1,m2,m3,error
from mas.MAS import run_simulation

f = spea_f_builder(mac1, mac2)



def run_spea(f, generacion, poblacion,simulaciones,y_true):
    M1 = 0
    M2 = 0
    M3 = 0
    ERROR = 0
    super_pareto = []
    for i in range(simulaciones):
        pareto_set = spea(poblacion, generacion, f)
        pareto_set = [{"f1": org[0],"f2": org[1]} for org in map(f, pareto_set)]
        super_pareto = super_pareto + pareto_set
    return super_pareto

def run_mas():
    super_pareto = []
    for i in range(1):
        pareto = run_simulation(20,100,'./datasets/tsp_kroac100.tsp.txt')
        super_pareto = super_pareto + pareto
    return super_pareto
f = spea_f_builder(mab1, mab2)
pareto_spea = run_spea(f,100,100,1,Y_TRUE_KROAC)
pareto_mas = run_mas()
plt.plot([x['f1'] for x in pareto_spea],[y['f2'] for y in pareto_spea],'o', color='yellow')
plt.plot([x['f1'] for x in pareto_mas],[y['f2'] for y in pareto_mas],'o', color='blue')
plt.plot([x['f1'] for x in Y_TRUE_KROAC],[y['f2'] for y in Y_TRUE_KROAC],'o', color='red')
plt.show()
