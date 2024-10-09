#Ejercicio 3

a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))

#Se verifica que los valores ingresados sean positivos
if a <= 0 or b <= 0:
   print("Los valores ingresados tienen que ser positivos")
   exit()

#Se intercambian los valores si a < b
if a < b:
   a, b = b,a
   print("Se han intercambiado los valores: ahora a = " + str(a) + " y b = " + str(b))


#MCD con el algoritmo de Euclides  a= qb + r

while b != 0:  # Mientras b no sea 0 se ejecuta el ciclo
   r = a % b # Se calcula el residuo de la división de a entre b
   print(a, "=", b, "(", a // b, ")", "+", r) 
   a = b # Se asigna el valor de b a a
   print("a = ", a)
   b = r # Se asigna el valor de r a b
   print("b = ", b)

print("El MCD de los números ingresados es:", a)


