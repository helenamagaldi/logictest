from datetime 
import datetime 
import csv
import os

def cadastrar_cliente():
    print('\n------ CADASTRO DE CLIENTES ------\n') cadastro = {}
    nome = input("Nome.......: ")
    cpf = input("CPF........: ")
    rg = input("RG.........: ")
    cadastro[cpf] = [nome, rg] # dictionary

# generating file clientes.csv
    clientes_csv = open("clientes.csv","a") clientes_csv.write(f"{cpf};{nome};{rg}\n") clientes_csv.close()
    print('Cadastro realizado com sucesso!')


#clients list
def listar_clientes():
print('\n------ LISTAGEM DE CLIENTES ------\n') 
clientes_csv = open('clientes.csv')
dados = csv.DictReader(clientes_csv, delimiter = ';')

print(f'{"CPF":15}', f'{"NOME":30}',"RG") 
for cliente in dados:
    print(f'{cliente["cpf"]:15}', f'{cliente["nome"]:30}', cliente["rg"]clientes_csv.close()

# movies 
def cadastrar_filme():
print('\n------ CADASTRO DE FILMES/TÍTULOS ------\n') cadastro = {}
    cadastro = {}
    codigo = input("Codigo.......: ") 
    tipo = input("DVD/Fita.....: ")
    nome_filme = input("Titulo.......: ")
    ano_lancamento = input("Ano..........: ")

    cadastro[codigo] = [tipo,nome_filme,ano_lancamento] #dictionary

    filmes_csv = open("filmes.csv, "a")
    filmes_csv.write(f"{codigo};{tipo};{nome_filme};{ano_lancamento}\n)
    filmes_csv.close()

# listing all movies 
def listar_filmes():
    print('\n----- Lista de filmes -----\n')
    filmes_csv = open("filmes.csv")
    dados = csv.DictReader(filmes_csv, delimiter = ';')

    print(f'{CODIGO}:10', f'{TIPO}:10)', f'{"NOME DO FILME":30} , "ANO")
    for filme in dados:
            print(f'{filme["codigo"]:10', f'{filme["nome_filme"]:30}', filme["ano_lancamento])
    filmes_csv.close()


# movies 
def realizar_emprestimo():
    print('\n --- EMPRÉSTIMOS ---\n')
    cadastro = {}
    nome_usuario = input("Nome do cliente....: ")
    codigo_filme = input("Código do filme....: ")
    data_emprestimo = input("Data de empréstimo(dd/mm/aaaa)...: ")

    cadastro = {'nome_usuario': nome_usuario,'codigo_filme': codigo_filme, 'data_emprestimo': data_emprestimo}
    