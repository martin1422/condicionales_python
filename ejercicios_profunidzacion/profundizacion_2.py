# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

def calculo(numero):
    if (numero % 2) == 0:
        print('El numero ingresado es par')
    else:
        print('El numero ingresado es impar')    
    return



print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('Ingrese tres numeros enteros:')
print('numero 1:')
numero_1 = int(input())
calculo(numero_1)

print('numero 2:')
numero_2 = int(input())
calculo(numero_2)

print('numero 3:')
numero_3 = int(input())
calculo(numero_3)
