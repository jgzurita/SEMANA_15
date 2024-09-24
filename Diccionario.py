### UEA ###
##JUAN ZURITA
#AGREGAMOS DICCIONARIO
informacion_personal = {
    "nombre": "Juan Zurita",
    "edad": 26,
    "ciudad": "orellana",
    "profesion": "tecnico"
}

# Modificamos la ciudad y profesion
informacion_personal["ciudad"] = "tena"
informacion_personal["profesion"] = "agricultor"

# Verificar si existe telefono y agregar de no ser el caso
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave edad
del informacion_personal["edad"]

