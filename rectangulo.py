# Pedir al usuario que ingrese el ancho y largo del rectángulo
ancho = float(input("Ingrese el ancho del rectángulo: "))
largo = float(input("Ingrese el largo del rectángulo: "))

# Calcular el área y perímetro del rectángulo
area = ancho * largo
perimetro = 2 * (ancho + largo)

# Imprimir los resultados del área y perímetro
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)

# Imprimir la gráfica del rectángulo
print("Gráfica del rectángulo:")
for i in range(int(largo)):
    for j in range(int(ancho)):
        print("*", end=" ")
    print()
