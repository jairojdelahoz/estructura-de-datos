word = input("Ingrese una palabra: ")
letter = input("ingrese una letra: ")

counter = 0

for l in word:
    if l == letter:
        counter += 1

print(f"La letra aparece {counter} veces")