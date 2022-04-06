coleccion = [1,2,3,4,5,6,7,8,9,1]
total_suma=sum(coleccion)
print("la suma de todo es",total_suma)

print("-----------------------")

cantidad_numeros= len(coleccion)
resultado_promedio = float(total_suma)/cantidad_numeros
print("El promedio es", resultado_promedio)

print("-----------------------")

pares =[]
impares = []
for colecciones in coleccion:
    if (colecciones%2)==0:
        pares.append(colecciones)
    else:
        impares.append(colecciones)
      

print("Lista de valores par",pares)
print("Lista de valores impar",impares)

print("-----------------------")

primos=[]
for coleciones in coleccion:
    bandera = True  
    numero = coleciones
    if numero > 1:
        for i in range(2,numero):
            if numero % i == 0:
                bandera = False
                break
        if bandera == True:
            primos.append(numero)

print("los valores primos de la lista son:",primos)  

print("-----------------------")
                
Numero_par=[]
Numero_impar=[]
for i in range(len(coleccion)):
    if (coleccion[i]%2)==0:
        Numero_par.append(i)
    else:
        Numero_impar.append(i)
print(coleccion)
print("Los numeros pares tienen las siguientes ubicaciones: ", Numero_par)
print("Los numeros impares tienen las siguientes ubicaciones: ", Numero_impar)
print("-----------------------")


coleccion.sort()
print("Ordenado de forma ascendente",coleccion)


coleccion.sort(reverse = True)
print("Ordenado de forma descendente",coleccion)
