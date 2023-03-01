'''
Datos:
    Álbum con 638 figuritas.
    Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
    Se compran las figuritas de manera individual.
    
Objetivo:
    ¿Cuántas figuritas hay que comprar para completar el álbum del Mundial?

'''
import random

def cuantas_figus(figus_total):
    album = [0]*figus_total
    contador = 0
    while sum(album)<figus_total:
        figu = random.randint(0,figus_total-1)
        contador = contador+1
        album[figu] = 1
    return contador

def promedio(lista):
    n_resultado = 0
    suma_resultados = 0
    while n_resultado < len(lista) :
        suma_resultados = suma_resultados + lista[n_resultado]
        n_resultado = n_resultado + 1
    return suma_resultados / len(lista)

def simular_muchas_repeticiones(n_rep, figus_total):
    lista_resultados = []
    contador = 0
    while contador < n_rep :
        lista_resultados.append(cuantas_figus(figus_total))
        contador = contador + 1
    return lista_resultados

'''
5. Utilizando la función simular_muchas_repeticiones con n_rep=1000,
estimar la cantidad media de figuritas que hay comprar para llenar
un álbum con figus_total=6. ¿Cuántas diría que hay que
comprar (en promedio) si el album tuviera figus_total=12 
guritas?
respuesta = promedio(simular_muchas_repeticiones(1000, 6)) 

15.185

6. Utilizando la función simular_muchas_repeticiones con n_rep=1000, 
estimar la cantidad media de figuritas que hay comprar para llenar
un álbum con figus_total=12. ¿Se condice con el resultado
anticipado?
respuesta = promedio(simular_muchas_repeticiones(1000, 12))

Si se condice, ya que es más del doble

37.005

7. Estimar la cantidad media de 
figuritas que hay comprar para llenar un álbum con figus_total=638.

respuesta = promedio(simular_muchas_repeticiones(1000, 638))
4507.803
'''


'''
-------------------------Sobre Chances-------------------------------
'''

def dame_chance(resultados, cantidad_maxima):
    contador = 0
    i= 0
    while i < len(resultados):
        if resultados[i]<= cantidad_maxima :
            contador = contador+1
        i = i+1
    chance=contador/len(resultados)
    return chance


muchos_resultados_album_de_6 = simular_muchas_repeticiones(1000, 6)

print(dame_chance(muchos_resultados_album_de_6, 11))
print(dame_chance(muchos_resultados_album_de_6, 15))

'''
Utilizando muchos_resultados_album_de_6, indique cuántas 
figuritas debería poder comprar para tener un 90 % de chances (prob=0.9) 
de completar el álbum.

Se debería poder comprar entre 22 y 24 figuritas (hay un error de decimales)

'''

def dame_figuritas(chance, resultados, figus_album):
    figuritas = figus_album-1
    while dame_chance(resultados, figuritas) < chance:
        figuritas = figuritas+1
    return figuritas

prueba1 = dame_figuritas(0.9, muchos_resultados_album_de_6, 6)
prueba2= dame_chance(muchos_resultados_album_de_6, prueba1)

print(prueba1)
print(prueba2)

'''
--------------------Para divertirte el fin de semana
Implemente una función dale_comprame(resultados, figus_total, prob) que tenga
por parámetros una lista llamada resultados, el tamaño del álbum, denotado
con figus_total y una probabilidad, denotada con prob (valor entre 0 y 1) que 
queremos tener de completar el álbum. Debe devolver la cantidad de figus
que tengo que comprar para completar un álbum con probabilidad prob, habiendo 
estimado las chance con los valores observados en la lista resultados.

'''

def dale_comprame(resultados, figus_total, prob):
    figuritas_compradas= figus_total-1
    if 0<=prob<=1:
        while dame_chance(resultados, figuritas_compradas)<prob:
            figuritas_compradas=figuritas_compradas+1
    return figuritas_compradas

print(dale_comprame(muchos_resultados_album_de_6, 6, 0.9))