def resultados(num, num2):
    cociente = num // num2
    resto = num % num2

    return resto, cociente

resto, cociente = resultados(30,15)

print("El resto es ",resto)
print("El cociente es ",cociente)