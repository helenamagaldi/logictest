# recebe um numero e tem que retornar 'true'
# se ele for PRIMO, 'false' se não for primo

numeroPrimo = input("Please type a numer: ")

if numeroPrimo > 1:
    for i in range (2,numeroPrimo):
        if (numeroPrimo % i) == 0:
            print(numeroPrimo, "is not a prime number")

    else:
        print(numeroPrimo, "is a prime number")

else:
    print(numeroPrimo, "is not a prime number")
