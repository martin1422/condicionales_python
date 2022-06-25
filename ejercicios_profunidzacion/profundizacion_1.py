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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('Ingrese 2 numeros')
print('numero 1: ')
numero_1 = int(input())
print('numero 2: ')
numero_2 = int(input())
resta = numero_1 - numero_2

print('Resultado = ', numero_1, ' - ', numero_2, ' = ', resta)

if resta == 0:
    print('Resultado de la resta es: ', resta, 'CERO')
elif resta > 0:
    print('Resultado de la resta es: ', resta, 'POSITIVO')
elif resta < 0:
    print('Resultado de la resta es: ', resta, 'NEGATIVO')
