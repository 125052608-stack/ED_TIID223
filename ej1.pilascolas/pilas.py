while True:
    pilas =[]
    while True:
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir\n")
        op = int(input("Elige una opcion\n"))

        match op:
            case 1: 
                num = input("Ingresa el número que deseas agregar\n")
                pilas.append(num)
                print(pilas)
            case 2: 
                if len(pilas) <=0:
                    print("No se puede borrar ningún elemento porque no hay ninguno dentro de la cola")
                else: 
                    pilas.popleft()
                    print("Nueva cola: \n",pilas)
            case 3:
                print("Cola actual \n",pilas)
            case 4:
                print("Dejaste de ejecutar el menú")
                break

    seguir = input("¿Quieres seguir ejecutando el programa? (Ss/Nn)\n")
    if (seguir == "N" or seguir == "n"):
        break
    elif  (seguir== "S" or seguir == "s"):
        print("Se continua el programa\n")