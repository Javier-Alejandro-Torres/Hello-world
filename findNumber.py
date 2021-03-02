import random                                   #Libreria random para generar numeros aleatorios
import os
file = open("GuessingSteps.txt", "w")
Numero_Random=random.randint(0,30)              #Numero random es igual a un numero random generado por la libreria con rango entre 0 y 30
                                                #Es necesario poner el rango a 31 porque si no, no pondría jamas el número 30

file.write('El sistema asigno el siguiente número random = %s'%Numero_Random + os.linesep + os.linesep)  #Guardo esta linea en el txt para saber el numero

i = 0       #Variable del contador
a=True      #Variable de la sentencia while


while a:                                                                                #Ciclo While
    try:                                                                                #Preferi poner excepciones para que no me pongan caracteres, solo exit y numeros
        Numero_magico = input("\nDame un Número: \n")                                   #Agrego la variable
        if (Numero_magico == "exit"):                                                   #Si es exit, entonces ...
            file.write("exit" + os.linesep + os.linesep)                                #Escribo exit en doc
            break                                                                       #Termina el juego
        Numero_Usuario = int(Numero_magico)                                             #si no es exit, el numero lo paso a entero porque lo tenia en string
        file.write('Numero_Usuario=%s'%Numero_Usuario + os.linesep + os.linesep)        #Escribo el numero del usuario
        i=i+1                                                                           #Contador para contar numero de intentos



        if (Numero_Usuario>Numero_Random):                                                                      #Si el num es muy grande entonces...
            print("Tu numero es muy grande, porfavor ingresa uno menor")                                        #escribe que es muy grande y devuelve al ciclo while
            file.write("Tu numero es muy grande, porfavor ingresa uno menor" + os.linesep + os.linesep )        #Escribe en el doc

        elif (Numero_Usuario<Numero_Random):                                                                    #Si el num es muy pequeño, entonces...
            print("Tu numero es muy pequeño, porfavor ingresa uno mayor")                                       #Escribe que es muy pequeño y devuelve al while
            file.write("Tu numero es muy pequeño, porfavor ingresa uno mayor" + os.linesep + os.linesep)        #Escribe que es muy pequeño en el doc

        elif (Numero_Usuario==Numero_Random):                                                                   #Si tu numero y el el random son iguales, entonces...
            print("Excelente, has acertado!!!!")                                                                #Acertaste
            print("Te ha tomado", i ,"intentos")                                                                #Menciona numero de intentos (sumatoria del contador)
            file.write("Excelente, has acertado!!!!" + os.linesep + os.linesep)                                 #Escribe en el doc
            file.close()                                                                                        #Cierra el doc
            break                                                                                               #Termine el programa

    except ValueError:                                                                                          #Catch como expect, si no es un valor numerico
            print("Ese no es un numero.  Prueba de nuevo")                                                      #Imprime prueba de nuevo

    except KeyboardInterrupt:                                                                                   #Si forzan el programa a terminar
            break                                                                                               #Termina el programa sin devolver error


