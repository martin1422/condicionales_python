# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(texto_1, ' es mayor a ', texto_2, ' en alfabeticamente')
else:
    print(texto_2, ' es mayor a ', texto_1, ' en alfabeticamente')

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
t1 = int(texto_1)
t2 = int(texto_2)


if t1 > t2:
    print(t1, ' es mayor a ', t2, 'numericamente')
else:
    print(t2, ' es mayor a ', t1, 'numericamente')

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

print(texto_1, ' En ascii es: ', ord(texto_1))
print(texto_2, ' En ascii es: ', ord(texto_2))
print("Dec hex  char\n" 
        "48	30	 0\n"
        "49	31	 1\n"
        "50	32	 2\n"
        "51	33	 3\n"
        "52	34	 4\n"
        "53	35	 5\n"
        "54	36	 6\n"
        "55	37	 7\n"
        "56	38	 8\n"
        "57	39	 9")
