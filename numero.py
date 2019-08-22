cant=input("digite la cantidad de numeros:")
suma=0
promedio=0
for i in range(1, cant+1):
    num=int(input("digite el numero"))
    suma=suma+num
    print("suma:",suma) 

promedio=suma/cant
print("promedio es igual:",promedio)
