import os
principiante=[]
avanzado=[]
experto=[]
opc=0
while opc!=4:
    try:
        opc=int(input("""
        1. Registrar puntajes torneo
        2. Listar los todos puntajes
        3. Imprimir por Tipo
        4. Salir del programa
        :"""))
    except:
        print("Opcion no valida")
    if opc == 1:
                tipo=input("Ingrese tipo jugador (principiante/avanzado/experto) :")
                if tipo == "principiante":
                    id=str(input("Id: "))
                    principiante.append=id
                    nombre=str(input("Nombre: "))
                    principiante.append=nombre
                    juego=str(input("Juego: "))
                    principiante.append=juego
                    puntajes=str(input("Puntaje: "))
                    principiante.append=puntajes
                elif tipo == "avanzado":
                    id=str(input("Id: "))
                    avanzado.append=id
                    nombre=str(input("Nombre: "))
                    avanzado.append=nombre
                    juego=str(input("Juego: "))
                    avanzado.append=juego
                    puntajes=str(input("Puntaje: "))
                    avanzado.append=puntajes
                elif tipo == "experto":
                    id=str(input("Id: "))
                    experto.append=id
                    nombre=str(input("Nombre: "))
                    experto.append=nombre
                    juego=str(input("Juego: "))
                    experto.append=juego
                    puntajes=str(input("Puntaje: "))
                    experto.append=puntajes
                else:
                    print("opcion invalida")
    elif opc == 2:
                print(principiante)
                print(avanzado)
                print(experto)
    elif opc == 3:
            categoria=input("ingrese categoria jugadores: ")
            if categoria == "principiante":
                print(f"imprimiendo lista jugadores categoria principiante")
                try:
                    puntaje = open("archivo.txt", "w")
                    puntaje.write(principiante)
                except:
                    print("Error en guardado de archivo")
            elif categoria == "avanzado":
                try:
                    print(f"imprimiendo lista jugadores categoria avanzada")
                    puntaje = open("archivo.txt", "w")
                    puntaje.write(avanzado)
                except:
                    print("Error en guardado de archivo")
            elif categoria == "experto":
                try:
                    print(f"imprimiendo lista jugadores categoria experto")
                    puntaje = open("archivo.txt", "w")
                    puntaje.write(experto)
                except:
                    print("Error en guardado de archivo")    
    else:
            print("Saliendo del programa")