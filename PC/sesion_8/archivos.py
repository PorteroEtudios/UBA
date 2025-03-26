# archivo = open("lafiesta.txt")
# lineas = archivo.readlines()
# archivo.close()

# contador = 0

# for linea in lineas:
#   print(linea)
#   if "nigga" in linea:
#     contador += 1

# print("La palabra nigga aparece", contador, "veces.")

archivo = open("unaCarpeta/personas.csv")
persona_cruda = archivo.readlines()
archivo.close()

#print(personas)


def transformar(persona):
  persona = persona.strip("\n")
  persona = persona.split(";")
  return persona


personas = list(map(transformar, persona_cruda))

suma_edades = 0
for persona in personas:
  [nombre, edad] = persona
  suma_edades += int(edad)

print(suma_edades / len(personas))
