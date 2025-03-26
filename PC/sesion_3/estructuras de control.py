# Estructuras de Control:
# Son estructuras que nos permiten controlar el flujo de nuestro código

# Estructuras Condicionales:
# - selectivas

# Estructura Selectiva IF:
# si pasa_tal_cosa entonces
    # hago esto

# llueve = False
# si llueve entonces
    # me abrigo

# hay_sol = True
# si hay_sol entonces
    # uso gorra

# if expresion:
    # accion_1
    # accion_2

hay_sol = True
hace_frio = True
if hay_sol and not hace_frio:
    print("voy a usar gorra, y no voy con buzo")
elif hay_sol and hace_frio:
    print("voy a usar gorra, y me voy con buzo")
elif not hay_sol and not hace_frio:
    print("no voy a usar gorra, y no voy con buzo")
else:
    print("no voy a usar gorra, y me voy con buzo")

def division(dividendo, divisor):
    if divisor == 0:
        return "error"
    
    return dividendo / divisor


# Estructuras Iterativas:
# mientras (condicion se cumple)
    # ejecutar ciertas acciones

paso = 1
while (paso<=10):
    print(paso)
    paso = paso + 1

for numero in range(1,11, 2):
    print(numero)