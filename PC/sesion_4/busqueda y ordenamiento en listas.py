def edad(persona):
    return persona[1]

personas = [
    ("Manola Bellido Mur", 34), 
    ("Bautista Lobo", 40), 
    ("Adolf Hitler", 38), 
    ("Cada Vez Maduro", 70)
]

resultado = ("Adolf Hitler", 38) in personas
print(resultado)

resultado = personas.index(("Cada Vez Maduro", 70))
print(resultado)

personas.sort(key=edad)

print(personas)