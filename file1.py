
def media():
    n1 = eval(input('N1'))
    n2 = eval(input('N2'))

    media = (n1+n2/2)
    if(media >6):
        return print("approved")
    else:
        return print("failed")

        # media() 