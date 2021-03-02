
def main():
    a = True
    while a:
        try:
            Decimal=int(input("Ingresa el numero Decimal a transformar: "))
            print("")
            print("El numero en binario es: ")
            binario(Decimal)
            print("")
            print("El numero en Hexadecimal es: ")
            Hexadecimal(Decimal)
            print("")


        except ValueError:
            print(" ")
            print("Porfavor solo ingresa numeros")

        except KeyboardInterrupt:
            break

def Hexadecimal(Decimal):
    while Decimal > 0:
        Residuo=Decimal%16
        Decimal=Decimal//16
        print(Cambio_Letra(Residuo), end="")


def Cambio_Letra(Letra):
    if Letra < 10:
        return Letra
    if Letra == 10:
        return "A"
    if Letra == 11:
        return "B"
    if Letra == 12:
        return "C"
    if Letra == 13:
        return "D"
    if Letra == 14:
        return "E"
    if Letra == 15:
        return "F"

def binario(Decimal):

    if Decimal == 0:
        print("0")
    bit = [ ]
    while Decimal:
        bit.append(Decimal % 2)
        Decimal >>= 1
    print(bit[::-1])

main()