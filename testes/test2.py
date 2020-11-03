# recebe um numero e tem que retornar 'true'
# se ele for PRIMO, 'false' se não for primo


numeroPrimo = input("Por favor escreva um numero primo ")

    for i in range(2, numeroPrimo):
        if ((numeroPrimo / 2 % i) == 0), False):
            print("false")
            break
    else: 
        print(numeroPrimo, "é um número primo")
    else:
    print(numeroPrimo, "não é um número primo")

Estrutura lógica:
- Verificar se número (int) do input é maior do que zero.
- Criar uma função com laço de repetição com as seguintes condições:
    - usar o range para determinar onde começa e onde termina o valor (no caso, a o próprio valor digitado)
    - checar se o número possui valor maior de 1.  Já delimitar que caso o valor seja igual a 1, a função possui valor verdadeiro.
    - como checar números primos: ter certeza que o valor do input é divisível por 2. Caso ocorra, consequentemente, a divisão do numero possui valor = 0 e a função possui valor falso. Neste caso, o programa deve retornar o valor false, visto que a checagem corresponde à procura por números primos.
    - laço de repetição deve ser terminado aqui.
- Caso a alternativa de fim do loop, onde o número seja divisível por 2 e com resto diferente de 0, o programa deve considerar o valor verdadeiro e o console deve retornar o valor de verdadeiro.
