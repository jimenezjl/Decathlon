#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 09:28:24 2023

@author: jose
"""
import random

max_shotput = 0

def attempt():
    global max_shotput
    total_shotput = []
    results = []
    for i in range(3):
        total_score = 0
        num_of_dice = 0
        print(f"INTENTO {i+1}/3")
        input("Pulsa enter para lanzar")
        while num_of_dice < 8:
            num_of_dice += 1
            dice_roll = random.randint(1, 6)
            total_score += dice_roll
            print(f"Dado {num_of_dice}: {dice_roll}, Suma: {total_score}")
            if dice_roll == 1:
                print(f"¡Has sacado un 1 en el dado {num_of_dice}! Tu lanzamiento se considera nulo.")
                total_score = 0
                break
            if num_of_dice == 8:
                total_shotput.append(total_score)
                results.append([i+1, total_score])
                print(f"Lanzamiento {i+1} terminado, puntuación total: {total_score}")
                if total_score > max_shotput:
                    max_shotput = total_score
                break
            response = input("Si quieres continuar lanzando, pulsa s, si quieres parar el lanzamiento pulsa n, (s/n): ")
            if response.lower() != 's':
                total_shotput.append(total_score)
                results.append([i+1, total_score])
                print(f"Lanzamiento {i+1} terminado, puntuación total: {total_score}")
                if total_score > max_shotput:
                    max_shotput = total_score
                break
        if total_score == 0:
            results.append([i+1, "Lanzamiento nulo"])
    print("Resultados:")
    for i, row in enumerate(results):
        if isinstance(row[1], int):
            if row[1] == max_shotput:
                print(f"Lanzamiento {row[0]}: \033[1m{row[1]}\033[0m (máximo)")
            else:
                print(f"Lanzamiento {row[0]}: {row[1]}")
        else:
            print(f"Lanzamiento {row[0]}: {row[1]}")
    return results

attempt()
