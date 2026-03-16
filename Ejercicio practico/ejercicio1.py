numbers = []

n = int(input("Ingrese el primer número: "))
numbers.append(n)

for i in range(4):
    n = int(input("Ingrese el siguiente número: "))
    numbers.append(n)

elderly = max(numbers)
minor = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Número mayor:{elderly}")
print(f"Número menor:{minor}")
print(f"El promedio:{average}")


