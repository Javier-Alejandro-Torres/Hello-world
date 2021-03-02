

#Definicion de a para estructura de control while
a=True

#Estructura repetitiva while
while a:
    #Control de excpciones try/catch, try/except
    try:

        Nombre_del_archivo = input("\nIngrese el nombre del archivo: \n")
        Arhivo = open(Nombre_del_archivo, "r")

        Nombre_de_la_palabra = input("\nDame una palabra a buscar: \n")
        Contador_de_ocurrencias =0
        z = 0

        for x in Arhivo:
            ocurrencias = x.count(Nombre_de_la_palabra)
            z = z + 1
            print("Ocurrencias en linea ", z, " : ", ocurrencias)

            Contador_de_ocurrencias = ocurrencias + Contador_de_ocurrencias
        print("")
        print("Numero de veces que salio la palabra en el texto: ", Contador_de_ocurrencias)

    except FileNotFoundError:
        print("Ese documento no lo tenemos, porfavor escriba otro")

    except KeyboardInterrupt:
        print("Gracias por buscar")