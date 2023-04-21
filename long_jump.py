#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:09:07 2023

@author: jose
"""
import random

# Primera parte del juego
print("¡Bienvenido a la prueba de salto de longitud!")
print("Comenzando la carrera. Recuerda. Guarda los dados con menor puntuación. Si la suma de los dados guardados supera 8, se considerará un salto nulo\n")

dados_totales = []
puntuacion = 0

while True:
    dados = [random.randint(1, 6) for _ in range(5 - len(dados_totales))]
    print("Has lanzado los dados:", dados)
    guardar = input("¿Qué dados quieres guardar? (ingresa números separados por espacios, o presiona Enter para guardar todos) ")
    if guardar:
        dados_guardados = [dados[int(i) - 1] for i in guardar.split()]
        dados_totales.extend(dados_guardados)
        dados = [dado for dado in dados if dado not in dados_guardados]
        print("Has guardado los dados:", dados_guardados)
        print(f'La suma de los dados que ya has guardado es {sum(dados_totales)}')
    else:
        dados_totales.extend(dados)
        print("Has guardado todos los dados")
        print(f'La suma de los dados que ya has guardado es {sum(dados_totales)}')
    if sum(dados_totales) > 8:
        print("Intento nulo, has superado 8 puntos")
        break
    if sum(dados_totales) >= 0:
        continuar = input("¿Quieres seguir jugando? (s/n) ")
        if continuar.lower() == 'n':
            break
    if len(dados_totales) == 4:
        print('Has tomado impulso con todos los dados. Suerte con el salto.')
        break

# Segunda parte del juego
if sum(dados_totales) <= 8:
    print("\n Es el momento del salto. Lanza los dados y quédate con al menos un dado con la mayor puntuación posible\n")

    puntuacion = 0
    dados_salto = dados_totales
    while dados_salto:
        dados = [random.randint(1, 6) for _ in range(len(dados_salto))]
        print("Has lanzado los dados:", dados)
        guardar = input("¿Qué dados quieres guardar? (ingresa números separados por espacios, o presiona Enter para guardar todos) ")
        if guardar:
            dados_guardados = [dados[int(i) - 1] for i in guardar.split()]
            dados_salto.extend(dados_guardados)
            puntuacion = sum(dados_salto)
            dados_salto = [dado for dado in dados_salto if dado not in dados_guardados]
            print("Has guardado los dados:", dados_guardados)
        else:
            #Sobra ese pop aquí, y hay que ver cómo ponerlo en el if guardar
            #puntuacion += dados_totales[0]
            puntuacion += sum(dados)
            dados_salto = 0
            #dados_totales.pop(0)
            print("Has guardado el dado restante")
        print("Tu puntuación actual es:", puntuacion)

    print("\nFin del juego, tu puntuación final es:", puntuacion)
else:
    print("\nFin del juego, intento nulo.")