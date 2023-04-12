#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:32:57 2023

@author: jose
"""
import random

height = 10
puntuacion = 0

while True:
    print("Estás en una altura de", height, "metros.")
    respuesta = input("¿Quieres saltar aquí (S) o esperar a la siguiente altura (E)? ")
    
    if respuesta.lower() == "s":
        num_dados = int(input("¿Cuántos dados quieres lanzar? (1-8): "))
        while num_dados < 1 or num_dados > 8:
            num_dados = int(input("Por favor, introduce un número válido de dados (1-8): "))
        intentos = 3
        while intentos > 0:
            dados = [random.randint(1, 6) for _ in range(num_dados)]
            suma_dados = sum(dados)
            print("Valores de los dados:", dados)
            if 1 in dados:
                print("Has sacado un 1, no puedes saltar. Tu puntuación es", puntuacion)
                break
            print("La suma de los dados es:", suma_dados)
            if suma_dados > height:
                print("¡Saltaste desde una altura de", height, "metros!")
                puntuacion = height
                break
            else:
                input("No has conseguido saltar. Pulsa enter e inténtalo de nuevo.")
                intentos -= 1
        else:
            print("Has fallado los tres intentos. Tu puntuación es", puntuacion)
            break
    
    height += 2

print("Tu puntuación final es", puntuacion)
