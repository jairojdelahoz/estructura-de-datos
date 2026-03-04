#Crear una cadena
texto = "Python es genial"

#Longitud de la cadena
print("Longitud:", len(texto))

#Acceder a caracteres por indice 
print("Primer carácter:" , texto[0])
print("Segundo carácter:" , texto[1])
print("Último carácter:" , texto[-1])
print("Penúltimo carácter:" , texto[-2])

#Recorrer la cadena
for letra in texto:
    print(letra)

#Subcadenas
print("Primeras 6 letras:" , texto[0:6])
print("Desde la posición 7 hasta la última:" , texto[7:])
print("Cadena al réves:" , texto[::-1])

#Metodos de cadenas
print("Mayúsculas:" , texto.upper())
print("Minúsculas:" , texto.lower())
print("Capitalizado:" , texto.capitalize())
print("Remplazar palabra:" , texto.replace('genial', 'increible'))

#Buscar dentro de la cadena
print("Posición de 'es':" , texto.find('es'))

#Verificar contenido
print("¿Empieza con Python?:" , texto.startswith("Python"))
print("¿Termina con genial?:" , texto.endswith("genial"))



