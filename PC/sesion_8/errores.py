

def edad_usuario():    
    es_correcta = False
    while (not es_correcta):
        try:
            print("ingrese su edad: ")
            edad = int(input())
            es_correcta = True
        except:
            print("no ingresaste un entero")
    return edad


edad = edad_usuario()
print("la edad ingresada x el usuario es: ", edad)
print(type(edad))