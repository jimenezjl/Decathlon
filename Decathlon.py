#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:47:34 2020

@author: jose
"""


import random

jugadores = []
#numplay = ()
print ('¿Cuántos jugadores sois?')
# AÑADIR CÓDIGO PARA INPUTS NO DESEADOS
numplay = int(input())
if numplay == 1:
    print ('Ánimo, jugador solitario.')
    print ('¿Cómo te llamas?')
    player = numplay
    jugadores.append(input())
else:
    for player in range (numplay):
        #jugadores = []
        print('¿Cómo se llama el jugador '+str(player+1)+'?')
        jugadores.append(input())

print('Estos son los jugadores de este Decathlon')     
for player in range(numplay):
    print(jugadores[player])



# 100 METROS LISOS
print('COMIENZAN LOS 100 METROS LISOS')
print('Cada jugador dispone de 2 conjuntos de 4 dados y 8 lanzamientos en total. Ningún 6 es válido')
for player in range(numplay):
    print('Es el turno de'+jugadores(player))
    
