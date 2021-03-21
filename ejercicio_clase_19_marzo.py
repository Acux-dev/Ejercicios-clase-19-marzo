#ejercicio 1
for x in range(10):
  print(x)

#ejercicio 2
for x in range(100,200):
  print(x)

#ejercicio 3
for x in range(5,21,3):
  print(x)

#ejercicio 4
n=int(input("Número: "))
for x in range(n, n*2):
    print(x)

#ejercicio 5
frase=input("Ingrese la frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase:
    print(x)

#ejercicio 7
total=0
for i in range(101):
    total=total+i
print("La sumatoria de los numeros entre 0 y 100 es:", total)

#ejercicio 8
añoInicio=int(input("Ingrese el Año inicial:"))
añoFin=int(input("Ingrese el Año final:"))
for año in range(añoInicio, añoFin+1):
   if not año%10==0:
       continue
   if not año%4==0:
       continue
   if año%100!=0 or año%400==0:
       print(año)

#ejercicio 9
N=int(input("Ingrese el número:"))
f=1
if N!=0:
    for i in range(1,N+1):
        f=f*i
print("El factorial es:", f)

#ejercicio 10
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3