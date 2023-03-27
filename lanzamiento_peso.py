#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 09:28:24 2023

@author: jose
"""
import random

total_score = 0
total_shotput = []
max_shotput = 0

def roll_dice():
    global total_score
    num_of_dice = 0
    while num_of_dice < 8:
        num_of_dice += 1
        dice_roll = random.randint(1, 6)
        total_score += dice_roll
        print(f"Dado {num_of_dice}: {dice_roll}, Suma: {total_score}")
        if dice_roll == 1:
            print(f"¡Has sacado un 1 en el dado {num_of_dice}! Tu lanzamiento se considera nulo.")
            return 0
        if num_of_dice == 8:
            return total_score
        response = input("¿Deseas lanzar otro dado? (s/n): ")
        if response.lower() != 's':
            return total_score

def attemp():
    total_attemp = 0
    global total_shotput
    while total_attemp < 3:
        total_attemp += 1
        print(f"Estás en el intento {total_attemp} de 3.")
        total_score = roll_dice()
        total_shotput.append(total_score)
        return total_shotput

    print(f"Los resultados de tus 3 intentos son: {total_shotput}")
 

attemp()

max_shotput = max(total_shotput)

print (f"Tu lanzamiento más largo ha sido {max_shotput}")