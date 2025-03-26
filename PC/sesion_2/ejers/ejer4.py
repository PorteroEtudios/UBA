def edad():
    año_Nac = int(input("Ingrese su año de nacimiento: "))
    año = int(input("Ingrese otro año cualquiera: "))

    edadEnAño = año - año_Nac
    return edadEnAño

edadCalculo = edad()
print("Tenias ", edadCalculo)