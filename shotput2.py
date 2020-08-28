#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:19:29 2020

@author: Bea
"""
import random

resultados = []

for tirada in range(8):
    dado = random.randint(1, 6)
    if dado == 1:
        print('El resultado de tu dado número '+str(tirada+1)+' es '+str(dado))
        print('Ya no puedes seguir tirando dados, tu lanzamiento ha sido nulo.')
        break
    else:
        resultados.append(dado)
        print('El resultado de tu dado número '+str(tirada+1)+' es '+str(dado))
        print('El total, por el momento, de tu lanzamiento es '+str(sum(resultados))+' puntos.')
        print('¿Quieres continuar lanzando dados? (s/n)')
        respuesta = input('s/n')
        
        if respuesta == 'n': break
            
if dado != 1:
    print('El resultado final de tus '+str(len(resultados))+' tiradas ha sido de '+str(sum(resultados))+' puntos.')
    
