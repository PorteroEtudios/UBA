def resultados():
    num = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    suma = num + num2
    resta = num - num2
    multiplicacion = num * num2
    division = num / num2
    resto = num % num2

    return suma, resta, multiplicacion, division, resto

suma, resta, multiplicacion, division, resto = resultados()

print("La suma es ",suma)
print("La resta es ",resta)
print("La multiplicacion es ",multiplicacion)
print("La division es ",division)
print("El resto es ",resto)