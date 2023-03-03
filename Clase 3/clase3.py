
"""
Created on Wed Mar  1 09:02:54 2023

@author: Exactas_Programa
"""

'''
-------------------------------Incendio forestal------------------------------
'''

import random
import matplotlib.pyplot as plt
import numpy as np

def generar_bosque(n):
    bosque = [0]*n
    return bosque 

def suceso_aleatorio(p):
    num=random.randint(1, 100)
    if num<=p :
        sucede= True
    else:
        sucede = False
    return sucede

def brotes(bosque, p):
    for i in range(0, len(bosque)):
        brota = suceso_aleatorio(p)
        if brota == True:
            bosque[i]=1
        else:
            bosque[i]=0
    return bosque

def cuantos(bosque, tipo_celda):
    cantidad = 0
    for i in range(0, len(bosque)):
        if bosque[i] == tipo_celda:
            cantidad = cantidad+1
    return cantidad
    
def rayos(bosque, f):
    for i in range(0, len(bosque)):
        rayo = suceso_aleatorio(f)
        if (rayo == True) and (bosque[i]==1):
            bosque[i]=-1
    return bosque

def propagacion(bosque):
    for i in range(0,len(bosque)):
        for i in range(0, len(bosque)):
            if bosque[i]==-1:
                if (i-1>=0) and bosque[i-1]==1:
                    bosque[i-1]=-1
                if (i+1<len(bosque)) and bosque[i+1]==1:
                    bosque[i+1]=-1
    return bosque
            
def limpieza(bosque):
    for i in range(0,len(bosque)):
        if bosque[i]==-1:
            bosque[i]=0
    return bosque

def dinamica(n,a, p, f):
    bosque = generar_bosque(n)
    t=0
    arboles_por_año =[]
    while t<a:
        brotes(bosque, p)
        rayos(bosque, f)
        propagacion(bosque)
        limpieza(bosque)
        arboles_por_año.append(cuantos(bosque, 1))
        t=t+1
    return sum(arboles_por_año)/a
'''
8-¿Cuál es el valor óptimo de p (el que da lugar a una producción
máxima de árboles) para una probabilidad f=2 % de caída de rayos?
Para eso, corra el programa de la dinámica forestal para
diferentes valores de p, a lo largo de 500 años, variando p del 0 % al 100 % 
como se mencionó en laclase. Gracar este análisis.
Nota: Importar el paquete pyplot con: import matplotlib.pyplot as plt
'''

probs=[]
promedios=[]
valores_p= np.arange(0,101,1)
for i in range(len(valores_p)):
    probs.append(valores_p[i])
    promedios.append(dinamica(100, 500, probs[i], 2))
    
plt.title("Árboles por año en función de la probabilidad de brote")
plt.xlabel("Probabilidad de brote", fontsize=16)
plt.ylabel("Promedio de árboles por año", color="blue")
plt.plot(probs, promedios,".")
plt.show()


'''
-------------------------------------Optativos--------------------------------

-----------------Dinámica evolutiva

'''
def brotesp_celda(bosque):
    pes = []
    for i in range(0, len(bosque)):
        p =random.randint(0, 100)
        pes.append(p)
    return pes

def actualizar_p(bosque_con_rayos, brotesp):
    pes = brotesp
    for i in range(0,len(bosque_con_rayos)):
        if bosque_con_rayos[i] == 1 and pes[i]<95:
            pes[i]= pes[i]+5
        elif bosque_con_rayos[i]==-1 and pes[i]>5:
            pes[i]=pes[i]-5
    return pes

def brotes_celda(bosque, brotesp):
    for i in range(0, len(bosque)):
        brota = suceso_aleatorio(brotesp[i])
        if brota == True:
            bosque[i]=1
        else:
            bosque[i]=0
    return bosque

def dinamica_evolutiva(n,a,f):
    bosque = generar_bosque(n)
    arboles_por_año =[]
    pes= brotesp_celda(bosque)
    e= 0
    for i in range(0,a):
        brotes_celda(bosque, pes)
        rayos(bosque, f)
        propagacion(bosque)
        pes=actualizar_p(bosque, pes)
        limpieza(bosque)
        arboles_por_año.append(cuantos(bosque, 1))
        if e < len(bosque)-1:
            e = e+1
    return sum(arboles_por_año)/a

'''
--------------Comparación de promedios dinámica simple y evolutiva
probs=[]
promedios=[]
valores_p= np.arange(0,101,1)
for i in range(len(valores_p)):
    probs.append(valores_p[i])
    promedios.append(dinamica(100, 500, probs[i], 10))
print(promedios) 

[Out]: [0.0, 0.936, 1.956, 2.908, 3.988, 4.918, 6.144, 7.014, 7.634, 8.914, 9.676, 10.612, 11.58, 12.682, 13.658, 14.606, 15.91, 16.582, 17.228, 18.414, 19.53, 19.93, 21.212, 22.292, 22.858, 24.128, 25.138, 26.096, 26.908, 27.838, 28.694, 30.134, 30.878, 32.124, 32.61, 33.132, 34.282, 35.578, 36.346, 37.21, 38.216, 39.0, 40.166, 40.978, 41.794, 42.372, 43.738, 44.44, 45.29, 46.312, 47.534, 47.98, 48.916, 49.716, 50.286, 51.444, 52.142, 52.734, 54.45, 55.11, 54.974, 56.326, 57.038, 57.892, 58.824, 59.24, 60.034, 61.058, 61.428, 61.75, 62.432, 63.574, 64.314, 64.778, 64.428, 65.326, 67.046, 66.392, 65.978, 67.036, 68.018, 67.968, 67.772, 67.78, 68.08, 68.426, 68.364, 67.126, 65.848, 66.644, 66.652, 64.38, 62.49, 59.518, 57.868, 54.464, 51.392, 45.274, 37.76, 27.45, 13.4]

promedios2 = []
for i in range(0, 101):
    promedios2.append(dinamica_evolutiva(100, 500, 10))
print(promedios2)
[Out]: [69.41, 63.994, 63.302, 63.098, 61.538, 63.462, 68.34, 64.118, 64.33, 62.59, 62.082, 65.404, 66.446, 64.704, 62.592, 61.846, 64.476, 64.876, 63.258, 62.518, 64.1, 63.454, 64.168, 63.718, 63.028, 63.676, 66.168, 67.01, 63.294, 63.236, 62.35, 66.636, 64.16, 64.528, 60.986, 61.68, 63.44, 63.276, 64.61, 62.262, 67.566, 62.578, 64.542, 63.096, 63.62, 64.45, 65.002, 63.792, 65.22, 67.446, 66.066, 62.18, 64.564, 64.092, 66.352, 63.766, 63.454, 66.254, 60.11, 66.736, 67.138, 65.098, 65.244, 62.606, 64.616, 61.748, 63.342, 63.446, 66.04, 64.154, 62.976, 63.012, 63.114, 63.914, 66.554, 65.29, 62.662, 62.946, 62.272, 64.232, 62.376, 65.11, 62.664, 63.262, 63.954, 62.074, 66.352, 61.58, 64.288, 62.618, 63.648, 66.268, 64.006, 65.564, 62.554, 65.32, 65.622, 65.814, 63.036, 63.156, 67.732]

-------------Comparación distribución final de p 
Dinamica evolutiva (por celda): [90, 90, 93, 91, 92, 90, 92, 90, 94, 94, 93, 92, 94, 90, 93, 92, 0, 91, 93, 93, 93, 93, 94, 93, 92, 93, 93, 93, 90, 91, 93, 85, 93, 94, 94, 90, 93, 92, 93, 77, 93, 94, 80, 90, 93, 93, 91, 92, 91, 93, 90, 93, 90, 92, 92, 0, 98, 97, 99, 98, 90, 85, 87, 89, 89, 90, 95, 96, 90, 86, 81, 87, 83, 82, 88, 88, 86, 88, 93, 98, 99, 98, 96, 98, 91, 97, 91, 93, 96, 91, 96, 96, 95, 97, 99, 95, 95, 88, 96, 95][90, 90, 93, 91, 92, 90, 92, 90, 94, 94, 93, 92, 94, 90, 93, 92, 0, 91, 93, 93, 93, 93, 94, 93, 92, 93, 93, 93, 90, 91, 93, 85, 93, 94, 94, 90, 93, 92, 93, 77, 93, 94, 80, 90, 93, 93, 91, 92, 91, 93, 90, 93, 90, 92, 92, 0, 98, 97, 99, 98, 90, 85, 87, 89, 89, 90, 95, 96, 90, 86, 81, 87, 83, 82, 88, 88, 86, 88, 93, 98, 99, 98, 96, 98, 91, 97, 91, 93, 96, 91, 96, 96, 95, 97, 99, 95, 95, 88, 96, 95]
Dinamica simple (por celda): [100]*100 
'''

años = []
promedios_por_año = []
for i in range(1,501):
    años.append(i)
    promedios_por_año.append(dinamica_evolutiva(100,i,10))
plt.plot(años, promedios_por_año)
plt.show()


'''
--------------------Otras dinámicas
'''

