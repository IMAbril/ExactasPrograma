"""
Created on Fri Mar  3 11:18:29 2023

@author: Abril
"""

'''
-------------------------------Clase 4: Avalancha------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt
import imageio
import os


#n= 6 tablero 8x8
t = np.repeat(0,8*8).reshape(8,8)
print(t[(1,1)])
t[(2,3)]=-1
print(t[(2,3)])
print(t.shape[0])
print(t.shape[1])
#2
def bordes(t):
    for i in range(t.shape[0]):
        t[(i,0)]=-1
        t[(0,i)]=-1
        t[(t.shape[0]-1,i)]=-1
        t[(i,t.shape[1]-1)]=-1
    return t
#3
def crear_tablero(n):
    t = np.repeat(0,n*n).reshape(n, n)
    bordes(t)
    return t 
#4
t1 = crear_tablero(9)    
print(t1)

#5
def es_borde(tablero, coord):
    es_borde=False
    if tablero[coord] == -1:
        es_borde=True
    return es_borde

#6
print(es_borde(t1, (0,1)))
print(es_borde(t1, (8,6)))
print(es_borde(t1, (5,6)))

#7
def tirar_copo(tablero, coord):
    tablero[coord]= tablero[coord]+1
    return tablero

#8
'''
a-(4,1) y (5,4)
b-  Vecinos de (4,1): (4,0) , (4,2) , (3,1) , (5,1)
    Vecinos de (5,4): (5,3) , (5,5) , (4,4) , (6,4)
'''

#9 
def vecinos_de(tablero, coord):
    vecinos = []
    if es_borde(tablero, (coord[0]+1,coord[1])) != True:
        vecinos.append((coord[0]+1,coord[1]))
    if es_borde(tablero, (coord[0]-1,coord[1])) != True:    
        vecinos.append((coord[0]-1,coord[1]))
    if es_borde(tablero, (coord[0],coord[1]+1)) != True:
        vecinos.append((coord[0],coord[1]+1))
    if es_borde(tablero, (coord[0],coord[1]-1)) != True:
        vecinos.append((coord[0],coord[1]-1))
    return vecinos

#10
print(vecinos_de(t1, (1,4)))
print(vecinos_de(t1, (2,5)))
print(vecinos_de(t1, (7,7)))

#11
def desbordar_posicion(tablero, coord):
    vecinos = vecinos_de(tablero, coord)
    if tablero[coord] >= 4:
        tablero[vecinos[0]] = tablero[vecinos[0]]+ 1
        tablero[vecinos[1]] = tablero[vecinos[1]]+ 1
        if len(vecinos)>2:
            tablero[vecinos[2]]= tablero[vecinos[2]]+ 1
            if len(vecinos)>3:
                tablero[vecinos[3]]= tablero[vecinos[3]]+ 1
        tablero[coord]= 0
    return tablero

#12
def desbordar_valle(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range(1, cantidad_filas-1):
        for j in range(1, cantidad_columnas-1):
            desbordar_posicion(tablero, (i,j))
    return tablero

#13
def hay_que_desbordar(tablero):
    hay_que_desbordar = False        
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range(1, cantidad_filas-1):
        for j in range(1, cantidad_columnas-1):
            if tablero[(i,j)] >= 4:
                hay_que_desbordar = True
    return hay_que_desbordar

#14
def estabilizar(tablero):
    while (hay_que_desbordar(tablero)):
        desbordar_valle(tablero)
    return tablero                
#15
def paso(tablero):
    filas_mitad = int((tablero.shape[0]-1)/2)
    columnas_mitad = int((tablero.shape[1]-1)/2)
    tirar_copo(tablero, (filas_mitad,columnas_mitad))
    estabilizar(tablero)
    return tablero

#16
def guardar_foto(t, paso):
    dir_name = "output"
    if not os.path.exists(dir_name): # me fijo si no existe el directorio
        os.mkdir(dir_name) #si no existe lo creo
    ax = plt.gca()
    file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
    plt.imshow(t, vmin=-1, vmax=3)
    ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
    plt.savefig(file_name)

def hacer_video(cant_fotos):
    dir_name = "output"
    lista_fotos=[]
    for i in range (cant_fotos):
        file_name = os.path.join(dir_name, "out{:05}.png".format(i))
        lista_fotos.append(imageio.imread(file_name))

    video_name = os.path.join(dir_name, "avalancha.mp4")
# genero el video con 10 Copos por segundo. Explorar otros valores:
    imageio.mimsave(video_name, lista_fotos, fps=10)
    print('Estamos trabajando en el directorio', os.getcwd())
    print('y se guardo el video:', video_name)

def probar(n, pasos=200):
    t = crear_tablero(n)
    for i in range(pasos):
        paso(t)
        guardar_foto(t, i)
    
    hacer_video(pasos)
    return t

