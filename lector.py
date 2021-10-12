def leer_txt(archivo):
    lines = []
    with open(archivo, 'r') as f:
        lines = f.readlines()
    return lines

def cargar_matriz(lines):
    mat1 = []
    mat2 = []
    for i in range(100):
        mat1.append(lines[2+i].split())
        mat2.append(lines[103+i].split())
    return mat1, mat2
    

a1 = 'tsp_KROAB100.TSP.TXT'
a2 = 'tsp_kroac100.tsp.txt'
l1 = leer_txt(a1)
l2 = leer_txt(a2)
mab1, mab2 = cargar_matriz(l1)
mac1, mac2 = cargar_matriz(l2)
print('fin')