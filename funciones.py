def menu(opc):
        while opc!=4:
            try:
                opc=int(input("""
                1. Registrar puntajes torneo
                2. Listar los todos puntajes
                3. Imprimir por Tipo
                4. Salir del programa
                : """))
            except:
                print("Opcion no valida")
        return(opc)        

def opciones(opc,principiante,avanzado,experto):
    if opc == 1:
            tipo=input(print("Ingrese tipo jugador (principiante/avanzado/experto) :"))
            if tipo == "principiante":
                principiante.append=input("Id")   
                principiante.append=input("Nombre")
                principiante.append=input("Juego")
                principiante.append=input("Puntaje")
                return(principiante)
            elif tipo == "avanzado":
                avanzado.append=input("Id")
                avanzado.append=input("Nombre")
                avanzado.append=input("Juego")
                avanzado.append=input("Puntaje")
                return(avanzado)
            elif tipo == "experto":
                experto.append=input("Id")
                experto.append=input("Nombre")
                experto.append=input("Juego")
                experto.append=input("Puntaje")
                return(experto)
            else:
                print("opcion invalida")
            return(principiante,avanzado,experto)
    elif opc == 2:
            print(principiante)
            print(avanzado)
            print(experto)
    elif opc == 3:
        if tipo == "principiante":
            print(f"imprimiendo lista jugadores categoria principiante")
            try:
                puntaje = open("archivo.txt", "w")
                puntaje.write(principiante)
                puntaje.close
            except:
                print("Error en guardado de archivo")
        elif tipo == "avanzado":
            try:
                print(f"imprimiendo lista jugadores categoria avanzada")
                puntaje = open("archivo.txt", "w")
                puntaje.write(avanzado)
                puntaje.close
            except:
                print("Error en guardado de archivo")
        elif tipo == "experto":
            try:
                print(f"imprimiendo lista jugadores categoria experto")
                puntaje = open("archivo.txt", "w")
                puntaje.write(experto)
                puntaje.close
            except:
                print("Error en guardado de archivo")    
    else:
        print("Saliendo del programa")





        