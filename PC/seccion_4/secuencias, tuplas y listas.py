# Secuencia: 
# son un conjunto de datos
# son un conjunto contiguo de memoria   
#  
# Strings:
# conjunto de caracteres, y son inmutables
# 
# Tuplas:
# son inmutables pero son un conjunto de datos de distintos tipos
# 
# Listas:
# permiten tenes tipos de datos distintos agruados, pero estas son mutables

tupla = ("Pensamiento", 56, 'a', [1,2])
lista= ["Pensamiento", 87, 475.3541, ["Pensamiento", "Computacional"]]


elemento_0_tupla = tupla[0]
print(elemento_0_tupla)


elemento_3_lista = lista[3]
print(elemento_3_lista[1])

fecha = [12, "Junio", 1970]

print(fecha)

dia, mes, anio = fecha

print(dia, mes, anio)


puntos = [
    (4,6),
    (8,2),
    (10, 5),
    (1, 1)
    (0, 7)
]

puntos.append((50,50))
puntos.insert(2, (80,80))
puntos.remove((0, 7))

for punto in puntos:
    x, y = punto
    print("x:", x, "- y:", y)



