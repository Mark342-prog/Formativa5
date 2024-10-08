#Ejercicio 3

a = int(input("a: Ingrese el numero a: "))
b = int(input("b: Ingrese el numero b: "))

if a < b:
   a, b = b,a
   print("Se han intercambiado los valores: ahora a = " + str(a) + " y b = " + str(b))


#MCD con el algoritmo de Euclides  a= mb + r

while b != 0:  # Mientras b no sea 0 se ejecuta el ciclo
   r = a % b # Se calcula el residuo de la división de a entre b
   a = b # Se asigna el valor de b a a
   b = r # Se asigna el valor de r a b

print("El MCD de los números ingresados es:", a)


