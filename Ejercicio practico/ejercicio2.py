def is_cousin(number):
    if number <= 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

n = int(input("Ingrese un número: "))

if is_cousin(n):
    print("Es primo")
else:
    print("No es primo")