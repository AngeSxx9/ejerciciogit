def min_max(valores):
  

    if len(valores) >0:
        menor = valores [0]
        mayor = valores [0]

        for n in valores:
            if n < menor:
                menor = n
            if n > mayor:
                mayor = n
        return menor,mayor
    else:
        return None

datos = [9,3,3,7,5,7,9,5,1]
print(min_max(datos))
