# Diccionarios en Python
# Codigo: Doctor Python

# Crear un Diccionario
diccio = {"Fruta":"uva", "edad":23, "llave_1":"python"}

# Acceder valores de tu diccionario usando las llaves
diccio["Fruta"]
diccio["llave_1"]

# Obtener todas las llaves de tu diccionario
diccio.keys()

# Obtener todos los elementos de tu diccionario
diccio.values()

# Añadir nuevos elementos tu diccionario key:value
diccio["nueva_llave"]= "nuevo valor"

# Modificar un elemento existente de tu diccionario
diccio["edad"]=34

# Eliminar un elemento 
del diccio["Fruta"]