# -*- coding: utf-8 -*-
"""
#Estudo de Caso: Biblioteca Comunitária



A biblioteca comunitária deseja informatizar o controle de empréstimos. Você foi contratado para desenvolver um programa em Python que simule esse processo.

##1.Cadastro de Usuário (20 pontos)
- Solicite o nome e a idade do usuário.
- Exiba uma mensagem de boas-vindas usando f-string e cores.
"""
nome = str(input('Digite seu nome: '))
idade = int(input('Digite seu idade:'))
print(f'\033[1;32mBem-vindo(a) {nome}! Você tem {idade} anos.\033[0m')

"""##2.Empréstimo de Livros (20 pontos)
O programa deve mostrar um menu opções de livros:
- Romance, Aventura, História
- Encerrar empréstimos
- O usuário escolhe digitando o número.
- Use if ou match-case para identificar o tipo de livro.
- Mantenha três contadores separados: romance, aventura, historia
- O total de livros emprestados não pode ultrapassar 5.
- Se o usuário tentar pegar mais de 5, mostrar: "Máximo de 5 livros atingido!" e sair da estrutura de repetição imediatamente.
"""

contador_supremo = 0
cont_romance = 0
cont_aventura = 0
cont_historia = 0
escolha = 'Y'

while escolha == 'Y':
    print('Você quer fazer um empréstimo? Y/N')
    escolha = str(input().upper())
    if escolha =='N':
        break
    else:
        print('Selecione seu livro para empréstimo: \n 1. Romance \n 2. Aventura \n 3. História \n 4. Encerrar empréstimo')
        opcao = int(input())
        if contador_supremo < 5: 
         match opcao:
                case 1:
                    cont_romance += 1
                    contador_supremo += 1
                case 2:
                    cont_aventura += 1
                    contador_supremo += 1
                case 3:
                    cont_historia += 1
                    contador_supremo += 1
                case _:
                    print('Programa de empréstimos encerrado')
                    break
        else:
            print('Você já tem 5 livros emprestados, encerrando o programa \n')
            break
    



"""##3.Relatório de Empréstimos (20 pontos)

Ao encerrar os empréstimos, o programa deve mostrar. Capriche na formatação:
- Nome do usuário
- Quantidade de livros de Romance
- Quantidade de livros de Aventura
- Quantidade de livros de História
- Total de livros emprestados
"""

print(f'\033[1;32m====Relatório de Empréstimos====\033[0m\n Nome do usuário: {nome}\nLivros de Romance:{cont_romance}\nLivros de Aventura: {cont_aventura}\nLivros de história: {cont_historia}\nTotal de livros emprestados: {contador_supremo}')

"""##4.Cadastro da Data de Entrega (20 pontos)

Após o relatório, a bibliotecária deve cadastrar a data de entrega de cada livro.
- Use um for que percorra de 1 até o total de livros emprestados.
- Em cada repetição, pedir: "Digite a data de entrega do livro i:", onde i é o numero do livro
- Exibir imediatamente a confirmação, por exemplo: "Data do livro i registrada: 12/05/2026"
"""
for i in range (1, contador_supremo + 1):
    data_entrega = input(f"Registre a data de entrega do livro {i} (DDMMYYYY): \n")
    dia = data_entrega[0:2]
    mes = data_entrega[2:4]
    ano = data_entrega[4:]
    data_formatada = f"{dia}/{mes}/{ano}"
    if ano < '2026' or mes >'12' or dia >'28':
        print(f"\033[1;31mA data do livro {i} é inválida. Por favor, registre uma data válida.\033[0m")
    else:
        print(f"O livro {i} tem a data de entrega: \033[1;32m{data_formatada}\033[0m")