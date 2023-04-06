import random

def diceroll():
    return random.randint(1, 6)

# Primer ciclo de lanzamientos
num_lanzamientos = 1
lanzamiento_valido = False
while num_lanzamientos <= 7 and not lanzamiento_valido:
    dados = [diceroll() for _ in range(4)]
    suma_dados = sum(dados)
    print(f"Resultado del lanzamiento {num_lanzamientos}: {dados}. Suma total: {suma_dados}")

    if 6 not in dados:
        guardar_resultado = input("¿Quieres guardar este resultado? (s/n): ")
        if guardar_resultado.lower() == 's':
            cincuentam = suma_dados
            lanzamiento_valido = True
        else:
            num_lanzamientos += 1
    else:
        print(f"Al menos uno de los dados ha sido un 6, debes volver a lanzar los dados. Recuerda que tienes un máximo de 7 lanzamientos y este es tu lanzamiento número {num_lanzamientos}")
        num_lanzamientos += 1

# Segundo ciclo de lanzamientos sin reiniciar el contador de lanzamientos
if lanzamiento_valido:
    suma_total = cincuentam
    while num_lanzamientos <= 7:
        dados = [diceroll() for _ in range(4)]
        suma_dados = sum(dados)
        print(f"Resultado del lanzamiento {num_lanzamientos}: {dados}. Suma total: {suma_dados + suma_total}")

        if 6 not in dados:
            guardar_resultado = input("¿Quieres guardar este resultado? (s/n): ")
            if guardar_resultado.lower() == 's':
                suma_total += suma_dados
                break
            else:
                num_lanzamientos += 1
        else:
            if num_lanzamientos == 7:
                print("Error: se ha alcanzado el máximo de lanzamientos y se ha obtenido un 6")
                break
            print(f"Al menos uno de los dados ha sido un 6, debes volver a lanzar los dados. Recuerda que tienes un máximo de 7 lanzamientos y este es tu lanzamiento número {num_lanzamientos}")
            num_lanzamientos += 1

    print(f"Suma total: {suma_total}")
