#Cadena de caracteres -> class str
from operator import truediv


mensaje = 'esto es un texto de prueba'
print(type(mensaje))
number_5 ='5'
print(type(number_5))
#Numéricos 
# - enteros   -> class int
numero = 5
print(type(numero))
negativo = -5
print(type(negativo))

# - flotantes -> class float
decimal = 2.4
print(type(decimal))

# - complejos -> class complex
#los numeros complejos tienen 2 partes 1)real 2)imaginario
complejo = 1 + 2j
print(type(complejo))
print(type(complejo.real))#nos retornara si es real
print(type(complejo.imag))#nos retornara si es imaginario

#boolenaos -> class bool 
#deben ir en mayúsculas
aprobado = True
dificil = False
suma = 4 + 5 == 10
print(type(aprobado))
print(type(dificil))
print(type(suma))