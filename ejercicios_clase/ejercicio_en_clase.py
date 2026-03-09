capital = int(input("Ingrese el capital que desea invertir: "))

tasa_anual = 0.15

tasa_mensual = (1 + tasa_anual) ** (1/12) - 1

ganancia = capital * tasa_mensual

print("La ganancia despues de un mes es de:" , int(ganancia))
print("el dinero total de un mes es de:" , int(ganancia + capital))


#ejercicio 2

print("-------- Ejercicio 2 ------------")

sueldo_base = int(input("Ingrese el sueldo base del vendedor: "))

venta1 = int(input("Ingrese el valor de la primera venta del mes: "))
venta2 = int(input("Ingrese el valor de la segunda venta del mes: "))
venta3 = int(input("Ingrese el valor de la tercera venta del mes: "))

comision = (venta1 + venta2 + venta3) * 0.10

sueldo_total = sueldo_base + comision

print("El sueldo total del vendedor es de:", round(sueldo_total))

#ejercicio 3

print("-------- Ejercicio 3 ------------")


compra = int(input("Ingrese el valor de la compra: "))

descuento = compra * 0.15

valor_total = compra - descuento

print("el cliente debera pagar un valor total de:" , round(valor_total) , " por su compra")

#Ejercicio 4

print("-------- Ejercicio 4 ------------")

parcial1 = float(input("Ingrese la nota obtenida en el primer parcial: "))
parcial2 = float(input("Ingrese la nota obtenida en el segundo parcial: "))
parcial3 = float(input("Ingrese la nota obtenida en el tercer parcial: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

examen_final = float(input("Ingrese la nota obtenida en el examen final: "))

trabajo_final = float(input("Ingrese la nota obtenida en el trabajo final: "))

calificacion_final = (promedio_parciales * 0.40) + (examen_final * 0.50) + (trabajo_final * 0.10)

print("calificacion final del alumno en la materia de algoritmo es de:" , round(calificacion_final, 1))
