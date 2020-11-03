# idéia inicial: verificar se números são primos ou não

def main():
    numero = input("Por favor digite um numero")
    se_verdadeiro(numero)

#definir uma função que adquira o valor inteiro por meio de input do usuário

def se_verdadeiro(a):
# definir função para considerar os números de input como primos ou não usando laço de repetição
# definir como valor inicial da função como verdadeiro  
    x = True
# verdadeiro corresponde à situação em que o resto da divisão do número por 2 corresponde é diferente de 0. 
# No caso em que o resto da divisão seja igual a 0 (==), o valor deve retornar como falso, considerando que o número neste caso não é primo.
# após ambas as considerações, o laço de repetição deve ser terminado
    for i in range(2, a):
        if a % i == 0:
            x = False
            break 

# considerando os valores de verdadeiro e falso, o console deve retornar diferentes sentenças
    if x:
        print("número primo")
    else:
        print("número não é primo")