while True:
#aqui inicia el bucle y el codigo
    print("""
    dime, cuantos numeros deseas ingresar:
    1) quiero ingresar 2 numeros
    2) quiero ingresar 3 numeros
    3) terminar codigo
    """)
    #Estas son las opciones 
    opcion= int(input("elige una opcion: "))

    if opcion == 1:    #esta es la primera opcion del codigo
        n1 = float(input("primer numero"))  #se pide ingresar el primer numero
        n2 = float(input("segundo numero")) #se pide ingresar el segundo numero
        if n1 > n2:  #aqui se decide si el segundo numero NO es mayor que el primero 
            print("el segundo numero NO es mayor que el primero")  #este print sale si la condicion se cumple 
            

    elif opcion == 2:   #esta es la segunda opcion del codigo
        n1 = float(input("primer numero")) #se pide ingresar el primer numero
        n2 = float(input("segundo numero")) #se pide ingresar el segundo numero
        n3 = float(input("tercer numero")) #se pide ingresar el tercer numero
        if n1>n2 or n1>n3:  #aqui se decide si el segundo y tercer numero NO es mayor que el primero 
            print("el segundo numero NO es mayor que el primero")
            print("el tercer numero NO es mayor que el primero")
            #Estos prints aparecen si las codiciones se cumplen

    elif opcion == 3:
        break  #aqui se quiebra el codigo y se termina el bucle 
    else:
        print("opcion incorrecta")  #esta es una opcion incorrecta
