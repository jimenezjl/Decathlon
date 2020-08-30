#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:13:33 2020

@author: jose
"""

import random

print('BIENVENIDOS A LA PRIMERA PRUEBA DEL DECATHLON: LOS 100 METROS LISOS')
print('¿Cómo se juega?')
print('Dispones de dos grupos de 4 dados y 7 tiradas en total.', 'Tras lanzar el primer grupo de dados puedes elegir si te gusta el resultado','y comienzas a lanzar el siguiente grupo','o si continúas lanzando el primer grupo.','Un resultado 6 en cualquier dado invalida ese lanzamiento.',sep=('\n'))
print('')
print('Pulsa Intro para lanzar tu primer grupo de dados.')
input()
for tirada in range (6):
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    dado3=random.randint(1,6)
    dado4=random.randint(1,6)
    sumatirada = dado1 + dado2 + dado3 + dado4
    print('El resultado de tu tirada '+str(tirada+1)+' ha sido '+str(dado1)+','+str(dado2)+','+str(dado3)+','+str(dado4)+'.')
    if tirada != 6:
        if dado1 == 6 or dado2 == 6 or dado3 == 6 or dado4 == 6:
            print('Tu tirada '+str(tirada+1)+' tiene un 6, así que tienes que volver a tirar.')
            input('Pulsa cualquier tecla para continuar')
        else:
            print('La suma total de tu tirada es '+str(sumatirada)+'.')
            print('¿Quieres repetir la tirada(s/n)')
            respuesta = input('s/n')
            if respuesta == 'n': break
    else:
        if dado1 == 6 or dado2 == 6 or dado3 == 6 or dado4 == 6:
            print('Tu tirada '+str(tirada+1)+' tiene un 6, así que tu resultado final es DNF.')
        else:
            print('El resultado final de tu carrera es '+str(sumatirada)+'.')
if tirada != 6:
    for tirada2 in range(6-tirada):
        dado5=random.randint(1,6)
        dado6=random.randint(1,6)
        dado7=random.randint(1,6)
        dado8=random.randint(1,6)
        sumatirada2 = dado5 + dado6 + dado7 + dado8
        sumatotal= sumatirada+sumatirada2
        print('El resultado de tu tirada '+str(tirada+1)+' ha sido '+str(dado5)+','+str(dado6)+','+str(dado7)+','+str(dado8)+'.')
        if tirada + tirada2 != 6:
            if dado5 == 6 or dado6 == 6 or dado7 == 6 or dado8 == 6:
                print('Tu tirada '+str(tirada+tirada2+2)+' tiene un 6, así que tienes que repetirla.')
                input('Pulsa cualquier tecla para continuar')
            else:
                print('La suma total de tu tirada es '+str(sumatirada2)+'.')
                print('El resultado de tu carrera sería '+str(sumatotal))
                print('¿Quieres repetir la tirada(s/n)')
                respuesta = input('s/n')
                if respuesta == 'n':
                    print('El resultado final de tu carrera es '+str(sumatotal)+'.')
                    break
                else:
                    if dado5 == 6 or dado6 == 6 or dado7 == 6 or dado8 == 6: 
                        print('Tu tirada '+str(tirada+tirada2+2)+' tiene un 6, así que tu resultado final es DNF.')
                        break
                    break