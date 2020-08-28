#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:13:33 2020

@author: jose
"""

import random

for tirada in range (5):
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    dado3=random.randint(1,6)
    dado4=random.randint(1,6)
    sumatirada = dado1 + dado2 + dado3 + dado4
    print('El resultado de tu tirada '+str(tirada+1)+' ha sido '+str(dado1)+','+str(dado2)+','+str(dado3)+','+str(dado4)+'.')
    if dado1 == 6 or dado2 == 6 or dado3 == 6 or dado4 == 6:
        print('Tu tirada '+str(tirada+1)+' tiene un 6, así que tienes que repetirla.')
        input('Pulsa cualquier tecla para continuar')
    else:
        print('La suma total de tu tirada es '+str(sumatirada)+'.')
        print('¿Quieres repetir la tirada(s/n)')
        respuesta = input('s/n')
        
        if respuesta == 'n': break

for tirada2 in range(5-tirada):
    dado5=random.randint(1,6)
    dado6=random.randint(1,6)
    dado7=random.randint(1,6)
    dado8=random.randint(1,6)
    sumatirada2 = dado5 + dado6 + dado7 + dado8
    sumatotal= sumatirada+sumatirada2
    print('El resultado de tu tirada '+str(tirada+1)+' ha sido '+str(dado5)+','+str(dado6)+','+str(dado7)+','+str(dado8)+'.')
    if dado5 == 6 or dado6 == 6 or dado7 == 6 or dado8 == 6:
        print('Tu tirada '+str(tirada+tirada2+1)+' tiene un 6, así que tienes que repetirla.')
        input('Pulsa cualquier tecla para continuar')
    else:
        print('La suma total de tu tirada es '+str(sumatirada2)+'.')
        print('El resultado de tu carrera sería '+str(sumatotal))
        print('¿Quieres repetir la tirada(s/n)')
        respuesta = input('s/n')
        
        if respuesta == 'n': break