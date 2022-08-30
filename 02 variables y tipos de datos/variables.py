#DECLARANDO VARIABLES EN PYTHON
#nombreVariable=valor
nombre_curso='python'
print('Bienvenido al curso de '+nombre_curso)

#podemos modificar la variable con otro valor
nombre_curso='JS'
print('Bienvenido al curso de '+nombre_curso)

#nuestra variable tomará el valor a través de un Input
nombre_curso=input('Ingrese el nombre del curso: ')
print('Bienvenido al curso de '+nombre_curso)

#podemos asignar un valor a múltiples variables
curso1 = curso2 = 'PHP'
print('Bienvenido al curso de '+curso1)
print('Bienvenido al curso de '+curso2)

#podemos asignar distintos valores a distintas variables, se debe mantener el orden
estudiante1,estudiante2,estudiante3 = 'Marco', 'Alan', 'Maria'
print('Los nombres de los estudinates son '+estudiante1,estudiante2,estudiante3,sep=' ')

#podemos imprimir nuestra variable dando formato al print (la letra f indica que se esta aplicando un formato)
mensaje='Marco Garcia'
print(f'Mi nombre es: {mensaje}')

#sin importancia