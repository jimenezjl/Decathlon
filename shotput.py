#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 08:59:32 2020

@author: jose
"""


#Lanzamiento de peso

import random

resultado = []
tirada=1
total = 0
dado = ()
'''
if tirada <= 9:
    dado(tirada)=random.randint(1, 6)
    if dado(tirada) == 1:
        Print('Tu tirada ha sido un 1, por lo tanto es un intento nulo')
        break
    break
    else
    print('El restultado de tu dado número '+tirada+' es'+dado(tirada))
    resultado = resultado + [dado(tirada)]
    print('¿Quieres continuar lanzando el siguiente dado? (Sí/No)')
    respuesta = input(S/N)
    tirada=tirada+1
    
    if respuesta != 'Si':
        break
'''    
while tirada <= 8 or dado!=1:
    # Descomenta para el azar o las pruebas con resultado fijo
    #dado = 5
    dado=random.randint(1, 6)
    if dado != 1 and tirada !=8:
        print('El resultado de tu dado número '+str(tirada)+' es '+str(dado))
        resultado=resultado+[dado]
        total=total+dado
        #Sumar todos los números de resultado
        print('Llevas '+str(total)+' puntos')
        tirada=tirada+1
        print('¿Quieres continuar lanzando dados? (S/N)')
        respuesta = input('s/n')
        if respuesta == 'n':
            print('Has terminado tu lanzamiento número (intento), con un total de '+str(total)+' puntos.')
            break
    elif tirada == 8:
        print('El resultado de tu dado número '+str(tirada)+' es '+str(dado))
        resultado=resultado+[dado]
        total=total+dado
        print('Has conseguido un total de '+str(total)+' puntos en tu lanzamiento.')
        break
    else:
        print('Tu lanzamiento ha sido un 1, por lo tanto tu intento en nulo')


    