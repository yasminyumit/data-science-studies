#Conjuntos
#Sao colecoes que nao permitem duplicados
#Porque NAO SAO INDEXADOS (posicionais) - NAO TEM ORDEM
#Eh como se tivessemos colocado os itens/elementos numa sacola
#Nao existe ALTERACAO DE ELEMENTO
#Mas podemos incluir e excluir elementos
#O simbolo é do dicionario {}

meujardim = {'rosa', 'camelia', 'geranio'}
print(type(meujardim))
#Ao exibir as informações do conjunto, o Python pode mudar a ordem
print(meujardim)

print('\nAdicionar')
#Nao ha garantias que ira adicionar o novo elemento no final
#Pois nao é posicional
meujardim.add('margarida')
print(meujardim)
#Como nao permite repetidos, se adicionar um item que ja existe, ele ignora
print('\nAdicionando repetidos')
meujardim.add('margarida')
meujardim.add('margarida')
meujardim.add('rosa')
print(meujardim)

#qual o uso em ciencia de dados?
#webscrapping
#varrer um texto e colocar os conectores da lingua portuguesa(e, ou, mas, a, o, os)
#e ir armazendo nessa colecao
#dai vai garantir que nao entra repetidamente esses elementos

print('\nEliminar ou Remover')
meujardim.remove('rosa')
print(meujardim)
meujardim.discard('geranio')
print(meujardim)
#retira um elemento aleatorio
meujardim.pop()
print(meujardim)

print('\nEliminando todos os itens do conjunto')
meujardim.clear()
#o conjunto vazio nao é representado pelo simbolo {} pois esse simbolo
#esta reservado para o dicionario
#o conjunto vazio apresenta-se com a palavra set()
print(meujardim)

print('\nJuntando Conjuntos')
meujardim = {'rosa', 'camelia', 'geranio'}
meuquintal = set(('pinheiro', False, 800, 'camelia'))
print(meujardim)
print(meuquintal)
print('\ne criando um novo conjunto')
# o union é usado para criar um conjunto novo
paisagismo = meuquintal.union(meujardim)
print(paisagismo)

#podemos querer acrescentar um conjunto no outro
print('\ne acrescentando um conjunto no outro')
print(meujardim)
print(meuquintal)
meuquintal.update(meujardim)
print(meuquintal)


print('\n intersecção de conjuntos')
meu_jardim = {"rosa", "tulipa", "margarida"}
floricultura = {"rosa", "orquídea", "margarida", "cravo", "tulipa"}

print('\n e criando um novo conjunto')
interseccao = floricultura.intersection(meu_jardim)
print('\n atualizando o conjunto')


#1. Crie um conjunto com os nomes da agenda a partir do dicionario abaixo
agenda= [{'nome': 'Pat', 'telefone': 1234}, 
{'nome': 'Antonia', 'telefone': 567},{'nome': 'Maria', 'telefone': 1940309238}]
#o método set() cria um conjunto a partir de uma lista, 
# tupla ou dicionario
resultado = set()
nomes = set() #
for contato in agenda:
    nomes.add(contato['nome'])
    resultado = nomes
print("conjunto de nomes:",resultado)




#2.
usuarios_ativos = {
    'Ana', 'Bruno', 'Carlos',
    'Daniela', 'Eduardo',
    'Fernanda', 'Gabriel'
}

usuarios_bloqueados = {
    'Carlos', 'Fernanda'
}

usuarios_admin = {
    'Ana', 'Carlos', 'Gabriel'
}

# Quais usuários estão ativos?
print(f'Usuários Ativos: {usuarios_ativos}')
# Quais usuários estão bloqueados?
print(f'Usuários Bloqueados: {usuarios_bloqueados}')
# Quais administradores estão ativos?
usuarios_admin_ativos = usuarios_admin.intersection(usuarios_ativos)
print(f'Administradores que estão ativos: {usuarios_admin_ativos}')
# Quais administradores estão bloqueados?
usuarios_admin_bloqueados = usuarios_admin.intersection(usuarios_bloqueados)
print(f'Administradores que estão bloqueados: {usuarios_admin_bloqueados}')
# Quais usuários ativos não são administradores?
usuarios_ativos_nao_admin = usuarios_ativos.difference(usuarios_admin)
print(f'Usuários ativos que não são administradores: {usuarios_ativos_nao_admin}')
# Quais usuários são administradores e não estão bloqueados?
usuarios_admin_nao_bloqueados = usuarios_admin.difference(usuarios_bloqueados)
print(f'Administradores que não estão bloqueados: {usuarios_admin_nao_bloqueados}')
# Quais usuários estão ativos e bloqueados simultaneamente?
usuarios_ativos_bloqueados = usuarios_ativos.intersection(usuarios_bloqueados)
print(f'Usuários que estão ativos e bloqueados simultaneamente: {usuarios_ativos_bloqueados}')
