#Colecoes
"""
Estruturas de dados dentro do python que armazena varios valores numa unica variavel, como por exemplo: 
listas, tuplas, dicionarios e conjuntos.

#Listas
- Mutáveis
- Indexáveis
- Ordenadas
- Permitem elementos duplicados
- Podem conter elementos de tipos diferentes
#Tuplas
- Imutáveis
- Indexáveis
- Ordenadas
- Permitem elementos duplicados

#Dicionários
- Mutáveis
- Não indexáveis
- Não ordenados
- Não permitem elementos duplicados
- Podem conter elementos de tipos diferentes

#Conjuntos
- Mutáveis
- Não indexáveis
- Não ordenados
- Não permitem elementos duplicados
- Podem conter elementos de tipos diferentes


"""

minhaLista = [1, 2, 3, 4, 5]

print(f'parte da lista: {minhaLista[0:3]}')
print(f'parte da lista: {minhaLista[2:]}')
print(f'parte da lista: {minhaLista[:3]}    ')
#Representacao do final da lista pode ser feita com : apenas

#o ultimo parametro é o pulo e funciona como funciona no range
print(f'parte da lista invertida pelo positivo: {minhaLista[::-1]}')
print(f'parte da lista invertida pelo negativo: {minhaLista[-1::-1]}')
print(f'parte da lista invertida pelo negativo: {minhaLista[-1:0:-1]}')
print(f'parte da lista invertida pelo negativo: {minhaLista[-1::-2]}') #pula de dois em dois  

"""Slicing em frases:"""
frase = 'Python é a melhor linguagem de todas'
print(f'Frase: {frase}')
palavras = frase.split()
print(f'Palavras: {palavras}')
print(f'Frase invertida: {palavras[::-1]}')
print(f'Pegando Python: {palavras[0]}')

#Exercício: receita de bolo
bolo = ['farinha', 'açúcar', 'ovos', 'leite', 'fermento']
complementos = ['chocolate', 'baunilha', 'coco', 'canela']
bolo_perfeito = bolo + complementos
print(bolo_perfeito)
bolo.extend(complementos)#adiciona os elementos de complementos na lista bolo
print(bolo)

#Percorrendo uma lista com for
for i in bolo_perfeito:
    print(i)

#Percorrendo uma lista pelo indice
for i in range(len(bolo_perfeito)):
    print(f'Índice: {i} - Ingrediente: {bolo_perfeito[i]}') 


#Percorrendo uma lista com while
contador = 0
while contador < len(bolo_perfeito):
    print(f'Índice: {contador} - Ingrediente: {bolo_perfeito[contador]}')
    contador += 1

#Percorrendo uma lista com list comprehension
print('Percorrendo a lista com list comprehension:')
[print(f'indice {i+1} - Ingrediente: {bolo_perfeito[i]}') for i in range(len(bolo_perfeito))]



#desafio: descobrir se dois ingredientes estão presentes na lista de ingredientes do bolo perfeito
if ['cereja', 'tr']  in bolo_perfeito:
    print('A cereja está presente na lista de ingredientes')

posicao_cereja = bolo_perfeito.index('cereja') if 'cereja' in bolo_perfeito else -1
print(posicao_cereja)

#SORT X SORTED
lista_aleatoria = [5, 2, 9, 1, 5, 6]
print(f'Lista original: {lista_aleatoria}')
print(f'Lista ordenada com sorted: {sorted(lista_aleatoria)}')#sorted retorna uma nova lista ordenada, sem modificar a lista original
print(f'Lista original após sorted: {lista_aleatoria}')
lista_aleatoria.sort()#ordena a lista original
print(f'Lista original após sort: {lista_aleatoria}')