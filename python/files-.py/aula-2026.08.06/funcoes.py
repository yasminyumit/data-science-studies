'''
Type hinting é uma funcionalidade do Python
que permite especificar o tipo de variáveis, 
parâmetros e valores de retorno de funções. 
Isso ajuda a tornar o código mais legível e facilita
a detecção de erros durante o desenvolvimento.
'''
def dobro(num: int) -> int: #type hint]
    """
    Isso é um docstring, que é uma string de documentação
    Essa função recebe um número inteiro como parâmetro 
    e retorna o dobro desse número.
    """
    return num * 2

print(dobro(5))


#type hinting com variáveis
nom = "Vini"
nome: str = "Vini" #type hint
print(nome)


#lambda function com type hinting
ldobro = lambda num:num*2
print(ldobro(9))

#aumento salário
def aumento_salário(salario:float) -> float:
    """
    Essa função recebe um salário como parâmetro
    e retorna o salário com um aumento de 10%.
    """
    if salario > 15000:
        return salario*1.07 #7%
    else:
        return salario*1.15 #15%
print(f'{aumento_salário(20000):.2f}')

lreajuste_salarial = lambda salario: salario*1.07 if salario >15000 else salario*1.15
print(f'{lreajuste_salarial(19000):.2f}')


#lambda e map reduce
#map aplica uma função a cada item de um iterável (como uma lista) e
#...retorna um novo iterável com os resultados.

def triplo(num:int) -> int:
    """
    Essa função recebe um número inteiro como parâmetro
    e retorna o triplo desse número.
    """
    return num*3
print(triplo(5))

muitos_numeros = [1,2,3,4,5]
triplos = [triplo(num) for num in muitos_numeros]
#list compreheension é uma forma concisa de criar listas em Python,
#...geralmente usada para aplicar uma função a cada item de um iterável.
print(triplos)

#map
triplos_map = map(triplo, muitos_numeros)
print(list(triplos_map)) #list() converte o map object em uma lista

#quintuplo com lambda e map
print(list(map(lambda num:num*5, muitos_numeros))) 



