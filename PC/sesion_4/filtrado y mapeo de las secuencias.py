# Map

def cortar_palabra(palabra):
    return palabra[:4]

palabras = [
    "otorrinolaringologo",
    "silla",
    "play",
    "pc"
]

palabras_cortas = map(cortar_palabra, palabras)

print(list(palabras_cortas))


def sumar_uno(numero):
    return numero + 1

numeros = [4, 5, 78, 6, 2]

nuevos_numeros = list(map(sumar_uno, numeros))

print(numeros)
print(nuevos_numeros)


#Filter

def es_palabra_corta(palabra):
    longitud = len(palabra)
    if (longitud < 5):
        return True
    else:
        return False
    
def es_palabra_larga(palabra):
    longitud = len(palabra)
    if (longitud < 5):
        return False
    else:
        return True

palabras_cortas = list(filter(es_palabra_corta, palabras))
palabras_largas = list(filter(es_palabra_larga, palabras))

print(palabras_cortas)
print(palabras_largas)

