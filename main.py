coleccion=[1,2,3,4,5]
resultado = sum(coleccion)
def suma():
    print("El resultado de la suma es",resultado)

def promedio():
    promedio= resultado/len(coleccion)
    print("El promedio es",promedio)

def pares():
    pares=[]
    impares=[]
    for coleciones in coleccion:
        if(coleciones%2)==0:
            pares.append(coleciones)
        else:
            impares.append(coleciones)
    print("La lista de los pares es",pares)
    print("La lista de los impares es",impares)

def primos():
    primos = []
    bandera = True
    for coleciones in coleccion:
        numero = coleciones
        if numero > 1:
            for i in range(2, numero):
                if numero % i == 0:
                    bandera = False
                    break
            if bandera == True:
                primos.append(numero)
    print("los valores primos de la lista son:", primos)

def pares():
    Numero_par = []
    Numero_impar = []
    for i in range(len(coleccion)):
        if (coleccion[i] % 2) == 0:
            Numero_par.append(i)
        else:
            Numero_impar.append(i)
    print(coleccion)
    print("Los numeros pares tienen las siguientes ubicaciones: ", Numero_par)
    print("Los numeros impares tienen las siguientes ubicaciones: ", Numero_impar)

def ordenAsc():
    coleccion.sort()
    print("Ordenado de forma ascendente",coleccion)

def ordenDesc():
    coleccion.sort(reverse = True)
    print("Ordenado de forma descendente",coleccion)


suma()
promedio()
pares()
primos()
pares()
ordenAsc()
ordenDesc()



