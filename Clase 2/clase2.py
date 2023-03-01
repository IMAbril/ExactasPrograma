#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:03:19 2023

@author: Exactas_Programa
"""
import random

def tirar_cubilete():
    dados = []
    i = 0
    while i<5:
        dados.append(random.randint(0,5))
        i = i + 1
    return dados

def cuantos_hay(elemento, lista_dados):
    aparece = 0
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == elemento :
            aparece = aparece + 1
        i = i + 1
    return aparece

def puntos_por_uno(lista_dados):
    cantidad_unos = cuantos_hay(1, lista_dados)
    if cantidad_unos == 0 :
        puntos = 0
    elif cantidad_unos == 1 or cantidad_unos == 2 :
        puntos = cantidad_unos * 100
    elif cantidad_unos == 3 :
        puntos = 1000
    elif cantidad_unos == 4 :
        puntos = 1100
    elif cantidad_unos == 5 :
        puntos = 10000
    return puntos

def puntos_por_cinco(lista_dados):
    cantidad_cinco = cuantos_hay(5, lista_dados)
    if cantidad_cinco == 0 :
        puntos = 0
    elif cantidad_cinco == 1 or cantidad_cinco == 2 :
        puntos = cantidad_cinco * 50
    elif cantidad_cinco == 3 :
        puntos = 500
    elif cantidad_cinco == 4 :
        puntos = 550
    elif cantidad_cinco == 5 :
        puntos = 600
    return puntos

def total_puntos(lista_dados):
    puntos_totales = puntos_por_uno(lista_dados)+puntos_por_cinco(lista_dados)
    return puntos_totales

def jugar_ronda(k):
    puntos_jugadores = []
    i = 0
    while i<k:
        puntos_jugadores.append(total_puntos(tirar_cubilete()))
        i = i+1
    return puntos_jugadores

def acumular_puntos(puntajes_acumulados, puntajes_ronda):
    puntajes_actualizados = []
    i = 0
    while i< len(puntajes_ronda):
        puntajes_actualizados.append(puntajes_acumulados[i]+puntajes_ronda[i])
        i = i + 1
    return puntajes_actualizados

def hay_10mil(puntajes):
    i = 0
    while (puntajes[i]<10000) and (i<len(puntajes)-1):
        hay_10mil = False
        i = i+1
    if puntajes[i] >= 10000:
        hay_10mil = True
    return hay_10mil


def partida_completa(k):
    puntos=[0]*k
    rondas = 0
    while hay_10mil(puntos) != True :
        rondas = rondas + 1
        puntos = acumular_puntos(puntos, jugar_ronda(k))
    return rondas

'''
10-Vamos ahora a utilizar las funciones implementadas para responder
las siguientes preguntas:
(a) En promedio, ¿cuántas rondas tiene una partida con k=10 jugadores?
(b) ¿Qué chances hay de terminar una partida con k=10 jugadores (que algún jugador
alcance los diez mil puntos) si solo tenemos tiempo para jugar a lo sumo 18 rondas?

Nrep = 10000 partidas completas
k = 10 jugadores
cant_rondas = lista de la cantidad de rondas obtenidas en las 10000 partidas

Para aproximar la probabilidad pedida se puede contar la cantidad de partidas
que terminan en a lo sumo 18 rondas, y dividir por la cantidad de partidas
jugadas totales. 

(A) rta= 46.944 = promedio_rondas(10,10000)
(B) rta= 0.0233 = dame_chance(10,18)

Anticipar qué resultados deberían obtener con k=20 jugadores.
Repetir la simulación, pero con k=20.
¿Los resultados obtenidos coinciden con los anticipados?
Rta= 0.0468, aproximadamente el doble debido a que son el doble de jugadores
'''

def promedio_rondas(k, nrep):
    cant_rondas=[]
    suma_rondas = 0
    for i in range(0, nrep):
        cant_rondas.append(partida_completa(k))
        suma_rondas = suma_rondas + cant_rondas[i]
    promedio = suma_rondas/nrep
    return promedio

def dame_chance(k, ronda_maxima):
    cant_rondas=[]
    ronda_contada = 0
    nrep= 10000
    for i in range(0, nrep):
        cant_rondas.append(partida_completa(k))
        if cant_rondas[i] <= ronda_maxima:
            ronda_contada = ronda_contada+1
    return ronda_contada/nrep