
def media():
    n1 = eval(input('Informe a nota 1:'))
    n2 = eval(input('Informe a nota 2:'))

    media = (n1+n2/2)
    if(media >6):
        return print("aprovado")
    else:
        return print("reprovado")

        # media() 