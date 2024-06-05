def sumar_2_numeros():
    num1= float(input("Ingrese 1er numero: "))
    num2= float(input("Ingrese 2do Numero: "))
    total= num1+num2
    print(f"Funcion: el total de la suma es: {total}")

def restar_2_numeros(num1: float=0, num2: float=0):

    total=num1-num2
    print(f"el total de la resta es: {total}")

def multiplicar_2_numeros():
    nro1=float(input("Ingrese 1er número: "))
    nro2=float(input("Ingrese 2do número: "))
    total=nro1*nro2
    return total

def dividir_2_numeros(p_nro1: int, p_nro2: int):
    total=p_nro1/p_nro2
    return total

def validar_numero():
    while True:
        try:
            num=float(input("Ingrese número: "))
            break
        except:
            print("Error!, debe ingresar un numero entero!")
    return num

def menu():
    print("""
1. Sumar 2 numeros
2. Restar 2 numeros
3. multiplicar 2 numeros
4. dividir 2 numeros
            
""")
    
def validar_opciones(opciones):
    while True:
        try:
            opc=int(input("Ingrese opcion: "))
            if opc in opciones:
                break
            else:
                print("Error!, opcion incorrecta!")
            
        except:
            print("Error!, Debe usar un numero entero!")
    return opc
