'''
Para vários tributos, a base de cálculo é o salário mínimo. Elabore um algoritmo 
que leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e 
imprimir quantos salários mínimos essa pessoa ganha; Lance tratamentos de 
exceção condizentes
'''
import math
salario_minimo = 1500
salario_pessoa = int(input('Digite o valor do seu salário: '))
try:
    qtde_salarios_minimos = math.floor(salario_pessoa/salario_minimo)
    print(f'Você ganha {qtde_salarios_minimos} salários mínimos.')
    if qtde_salarios_minimos < 1:
        raise ValueError('O valor do salário da pessoa deve ser maior que o salário mínimo.')
except ValueError as e:
    print(f'Erro: {e}')

1200