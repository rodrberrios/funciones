#funciones: def _____():
#               nombre (posibles parametros)
#           return valor/variable
import os
os.system("cls")

from funciones import *



#################################################################
menu()
opc=validar_opciones([1,2,3,4])

if opc==1:
    sumar_2_numeros()

elif opc==2:
    nro1=float(input("ingrese primer numero: "))
    nro2=float(input("Ingrese segundo número: "))
    restar_2_numeros(nro1,nro2)

elif opc==3:
    total=multiplicar_2_numeros()
    print(f"el total de la multiplicacion es: {total}")

elif opc==4:
    nro1=int(input("ingrese primer numero: "))
    nro2=int(input("Ingrese segundo número: "))
    
    lista=[]

    lista.append(dividir_2_numeros(nro1,nro2))

    
else:
    pass
