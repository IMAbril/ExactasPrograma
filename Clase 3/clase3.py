
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
