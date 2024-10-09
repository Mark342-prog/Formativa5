import math
#Ejercicio 1
# Función para generar números primos hasta un límite usando la criba de Eratóstenes
def Primos_N(n):
    if n < 2:
        return

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if prime[p]:
            # Marcar los múltiplos de p como no primos, comenzando desde p^2.
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Imprimir los números primos
    primes = [p for p in range(2, n + 1) if prime[p]]
    print(*primes)

# Función para determinar si un número n es primo utilizando la criba
def isprime(n):
    if n <= 1:
        return f"El número {n} no es primo."
    
    # Generar todos los primos hasta √n
    primos = criba_eratostenes(int(math.sqrt(n)))
    
    # Verificar si n es divisible por alguno de los primos
    for primo in primos:
        if n % primo == 0:
            return f"El número {n} no es primo, pues lo divide {primo}."
    
    return f"El número {n} es primo."
#Requisitos de la función eucliodiano

# Función principal para probar con varios números
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
