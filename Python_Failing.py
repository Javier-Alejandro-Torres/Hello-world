def main():

    palabra = input("Ingresa el numero: ")
    str_to_int(palabra)
    numero = int(input("Ingrese un numero:"))
    int_to_str(numero)


def str_to_int(palabra):
    resultado1=0
    for i in range(len(palabra)):

        if (palabra[i] == "1"):
            resultado = pow(10, len(palabra) - i)

        elif (palabra[i] == "2"):
            resultado = 2*pow(10, len(palabra) - i)

        elif (palabra[i] == "3"):
            resultado = 3 * pow(10, len(palabra) - i)

        elif (palabra[i] == "4"):
            resultado = 4 * pow(10, len(palabra) - i)

        elif (palabra[i] == "5"):
            resultado = 5 * pow(10, len(palabra) - i)

        elif (palabra[i] == "6"):
            resultado = 6 * pow(10, len(palabra) - i)

        elif (palabra[i] == "7"):
            resultado = 7 * pow(10, len(palabra) - i)

        elif (palabra[i] == "8"):
            resultado = 8 * pow(10, len(palabra) - i)

        elif (palabra[i] == "9"):
            resultado = 9 * pow(10, len(palabra) - i)

        elif (palabra[i] == "0"):
            resultado = 0 * pow(10, len(palabra) - i)

        resultado1=resultado+resultado1
        suma=resultado1/10
    print("De: "+ '"' + palabra + '"'+ " se transformo a:", round(suma))

def int_to_str(numero):
    output = []
    numero_guardado = numero
    while numero > 0:
        rem = numero % 10
        numero = int(numero / 10)
        output.append(rem)
        res = output[::-1]
    array = []
    for i in range(len(res)):

        if (res[i] == 1):
            array.append("1")
        elif (res[i] == 2):
            array.append("2")
        elif (res[i] == 3):
            array.append("3")
        elif (res[i] == 4):
            array.append("4")
        elif (res[i] == 5):
            array.append("5")
        elif (res[i] == 6):
            array.append("6")
        elif (res[i] == 7):
            array.append("7")
        elif (res[i] == 8):
            array.append("8")
        elif (res[i] == 9):
            array.append("9")
        elif (res[i] == 0):
            array.append("0")

    x = "".join(array)
    print("De:", numero_guardado,"se transformo a: " + '"' + x + '"')

if __name__ == "__main__":
    main()