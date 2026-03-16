def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i
    return result

n = int(input("Ingrese un número: "))

print("El factorial es: ", factorial(n))