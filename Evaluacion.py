while True:

    print("""
    dime, cuantos numeros deseas ingresar:
    1) quiero ingresar 2 numeros
    2) quiero ingresar 3 numeros
    3) terminar codigo
    """)
    opcion= int(input("elige una opcion: "))

    if opcion == 1:
        n1 = float(input("primer numero"))
        n2 = float(input("segundo numero"))
        if n1 > n2:
            print("el segundo numero NO es mayor que el primero")
            

    elif opcion == 2:
        n1 = float(input("primer numero"))
        n2 = float(input("segundo numero"))
        n3 = float(input("tercer numero"))
        if n1>n2 or n1>n3:
            print("el segundo numero NO es mayor que el primero")
            print("el tercer numero NO es mayor que el primero")


    elif opcion == 3:
        break
    else:
        print("opcion incorrecta")