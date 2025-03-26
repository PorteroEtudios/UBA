# ¿Qué es un diccionario?
# es una estructura q nos permite mapear un valor con uno o un grupo de datos

saludos = {
    "saludo_formal": "Buenos dias, ¿cómo se encuentra usted?",
    "saludo_informal": "Hola! ¿cómo estás?",
    "saludo_cumpleanios": "Feliz Cumple!"
}

print(saludos["saludo_cumpleanios"])

saludos["saludo_navidad"] = "Feliz navidad a todos!"

print(saludos["saludo_navidad"])

amigos = {
    "Juan": (25, "Marzo", "Nos conocimos en la primaria"),
    "Pedro": (28, "Diciembre", "Nos conocimos en un cumple"),
    "María": (30, "Marzo", "Nos conocimos en la facu"),
    "Ana": (28, "Noviembre", "No me acuerdo donde nos conocimos")
}

print(amigos.keys())

print(amigos.items())

amigos.update(
    {"Ana": (28, "Noviembre", "Nos conocimos en un plaza cuando eramos chicos")}
)