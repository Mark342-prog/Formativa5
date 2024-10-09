import math

def criba_eratostenes(limite):
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos
    
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    
    return [i for i, primo in enumerate(es_primo) if primo]


def isprime(n):
    if n <= 1:
        return f"El número {n} no es primo."
    
    # Generar todos los primos hasta √n
    primos = criba_eratostenes(int(math.sqrt(n)))
    
    
    for primo in primos:
        if n % primo == 0:
            return f"El número {n} no es primo, pues lo divide {primo}."
    
    return f"El número {n} es primo."


def main():
    while True:
        try:
            n = int(input("Ingrese un entero positivo n (o -1 para salir): "))
            if n == -1:
                break
            print(isprime(n))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Ejecutar las pruebas
main()
