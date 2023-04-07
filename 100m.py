import random

def diceroll():
    return random.randint(1, 6)

global num_lanzamientos, dados_guardados, pares_guardados, suma_total
num_lanzamientos = 1
dados_guardados = []
pares_guardados = 1
suma_total = 0

def lanzar_dados():
    global num_lanzamientos, dados_guardados, pares_guardados, suma_total
    lanzamiento_valido = False
    while num_lanzamientos <= 7 and pares_guardados < 3:
        print(f"Este es tu lanzamiento número {num_lanzamientos} y estás en tu ciclo de lanzamientos número {pares_guardados} de 2.")
        input("Pulsa enter para lanzar los dados.")
        dados = [diceroll() for _ in range(4)]
        suma_dados = sum(dados)
        print(f"Resultado del lanzamiento {num_lanzamientos}: {dados}. Suma del lanzamiento: {suma_dados} Suma total: {suma_total+suma_dados}")

        if 6 not in dados:
            guardar_resultado = input("¿Quieres guardar este resultado? (s/n): ")
            if guardar_resultado.lower() == 's':
                dados_guardados.append(dados)
                pares_guardados += 1
                num_lanzamientos += 1
                suma_total += suma_dados
                lanzamiento_valido = True
            else:
                num_lanzamientos += 1
        else:
            print(f"Al menos uno de los dados ha sido un 6, debes volver a lanzar los dados. Recuerda que tienes un máximo de 9 lanzamientos y este es tu lanzamiento número {num_lanzamientos}")
            num_lanzamientos += 1
    if lanzamiento_valido:
        return dados_guardados
    else:
        return None, num_lanzamientos
    
resultados = lanzar_dados()
if resultados:
    print(f"Los resultados válidos son: {resultados}")
else:
    print("No se ha guardado ningún resultado válido.")
print(f"La cantidad de pares de dados guardados es: {pares_guardados}")
print(f"El valor final de tu carrera de 100 metros lisos es: {suma_total}")
