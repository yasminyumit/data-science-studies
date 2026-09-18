# ecommerce.py
# Projeto de fundo - E-commerce simples
# Atividade avaliativa: dicionários, exceções (tratamento e lançamento)
# e arquivos de texto.
#
# Complete as funções marcadas com TODO. Não altere as funções já prontas
# (elas continuam funcionando exatamente como antes).
#
# As funções prontas têm type hints e docstring completa, no padrão que
# vocês devem seguir ao entregar a atividade. Nas funções com TODO, os
# comentários explicam o que a função deve fazer e o que representa
# cada argumento — cabe a vocês decidir como implementar, além de
# escrever os type hints e a docstring no mesmo padrão das prontas.

from functools import reduce

# ============================================================
# CONSTANTES
# ============================================================

# (Não há mais constantes de posição: produtos e usuários agora são
# representados como dicionários, então acessamos os campos pelo nome
# da chave, ex.: dados["preco"], dados["estoque"].)


# ============================================================
# SISTEMA — produtos (prontas, não alterar)
# ============================================================


def cadastrar_produto(catalogo: dict, nome: str, preco: float, estoque: int = 0) -> dict:
    """Cadastra um novo produto no catálogo.

    Args:
        catalogo: dicionário com os produtos do e-commerce. A chave é o
            nome do produto e o valor é um dicionário no formato
            {"preco": float, "estoque": int}.
        nome: nome do produto a ser cadastrado.
        preco: preço unitário do produto.
        estoque: quantidade disponível em estoque. Padrão: 0 (produto
            cadastrado sem estoque inicial).

    Returns:
        O catálogo atualizado, incluindo o novo produto.
    """

    
    catalogo[nome] = {"preco": preco, "estoque": estoque}
    return catalogo


def exibir_catalogo(catalogo: dict) -> None:
    """Exibe todos os produtos cadastrados no catálogo.

    Args:
        catalogo: dicionário com os produtos do e-commerce.

    Returns:
        None. Apenas imprime os produtos no console.
    """
    for nome, dados in catalogo.items():
        print(f"{nome} - R$ {dados['preco']:.2f} (estoque: {dados['estoque']})")


# ============================================================
# SISTEMA — produtos (implemente aqui)
# ============================================================


def calcular_valor_total_estoque(catalogo: dict) -> float:
    """Calcula o valor total investido em estoque.
 
    Soma, para todos os produtos do catálogo, o resultado de
    preco * estoque, usando reduce/lambda.
 
    Args:
        catalogo: dicionário com os produtos do e-commerce.
 
    Returns:
        O valor total investido em estoque (0.0 se o catálogo estiver
        vazio).
    """
    if not catalogo:
        return 0.0
    return reduce(
        lambda total, dados: total + dados["preco"] * dados["estoque"],
        catalogo.values(),
        0.0,
    )


def atualizar_estoque(catalogo: dict, nome_produto: str, quantidade: int) -> dict:
    """Atualiza a quantidade em estoque de um produto já cadastrado.
 
    Args:
        catalogo: dicionário com os produtos do e-commerce.
        nome_produto: nome do produto cujo estoque será atualizado.
        quantidade: quantidade a ser somada ao estoque atual (pode ser
            negativa, para representar uma saída de estoque).
 
    Returns:
        O catálogo atualizado.
 
    Raises:
        Exception: se o produto não existir no catálogo.
    """
    if nome_produto not in catalogo:
        raise Exception(f"Produto '{nome_produto}' não encontrado no catálogo.") 
    catalogo[nome_produto]["estoque"] += quantidade
    return catalogo



def listar_produtos_baixo_estoque(catalogo: dict, limite: int=10) ->list:
    """Lista os produtos cujo estoque está abaixo de um limite.
 
    Args:
        catalogo: dicionário com os produtos do e-commerce.
        limite: quantidade mínima de estoque considerada "segura".
            Padrão: 10.
 
    Returns:
        Lista com os nomes dos produtos cujo estoque está abaixo do
        limite informado.
    """
    produtos = [nome for nome, dados in catalogo.items() if dados['estoque'] < limite]
    return produtos
    


# ============================================================
# SISTEMA — usuários (implemente aqui)
# ============================================================


def email_existe(usuarios: dict, email: str) ->bool:
    """Verifica se já existe um usuário cadastrado com o e-mail informado.

    Args:
        usuarios: dicionário com os usuários cadastrados. A chave é o
            e-mail e o valor é um dicionário no formato
            {"nome": str, "senha": str}.
        email: e-mail a ser verificado.

    Returns:
        A mensagem "Email já cadastrado." se o e-mail já existir, ou
        None caso contrário.
    """ 
    if email in usuarios:
        return ("Email já cadastrado.")
    pass


def cadastrar_usuario(usuarios: dict, nome: str, email: str, senha: str) -> dict:
    """Cadastra um novo usuário no dicionário de usuários.

    Args:
        usuarios: dicionário com os usuários cadastrados.
        nome: nome do usuário.
        email: e-mail do usuário (usado como chave).
        senha: senha do usuário.

    Returns:
        O dicionário de usuários atualizado, incluindo o novo usuário.
    """
    usuarios[email] = {"nome": nome, "senha": senha}
    return usuarios


def fazer_login(usuarios: dict, email: str, senha: str) -> dict:
    """Verifica as credenciais informadas e retorna o resultado do login.

    Args:
        usuarios: dicionário com os usuários cadastrados.
        email: e-mail informado no login.
        senha: senha informada no login.

    Returns:
        Uma tupla ("Você está logado como", nome) se as credenciais
        conferirem; a string "Email  não cadastrado." se o e-mail não
        existir; ou a string "Senha incorreta" se a senha não conferir.
    """ 
    if email in usuarios and usuarios[email]["senha"] == senha:
        return ('Você está logado como', usuarios[email]["nome"])
    if email not in usuarios:
        return('Email  não cadastrado.')
    if senha != usuarios[email]["senha"]:
        return("Senha incorreta")



# ============================================================
# SISTEMA — arquivos (implemente aqui)
# ============================================================


def salvar_catalogo_em_arquivo(catalogo: dict, caminho: str) -> None:
    """Salva o catálogo em um arquivo de texto, uma linha por produto.
 
    Cada linha é gravada no formato "nome;preco;estoque".
 
    Args:
        catalogo: dicionário com os produtos do e-commerce.
        caminho: caminho do arquivo onde o catálogo será salvo.
 
    Returns:
        None.
    """ 
    with open (caminho, "w", encoding="utf-8") as arquivo:
        for nome, dados in catalogo.items():
            arquivo.write(f"{nome};{dados['preco']};{dados['estoque']}\n")


def carregar_catalogo_de_arquivo(caminho: str) -> dict:
    """Carrega um catálogo a partir de um arquivo de texto.
 
    Lê um arquivo no mesmo formato gerado por
    salvar_catalogo_em_arquivo ("nome;preco;estoque" por linha). Se o
    arquivo não existir, o erro é tratado internamente e um catálogo
    vazio é devolvido.
 
    Args:
        caminho: caminho do arquivo a ser lido.
 
    Returns:
        O catálogo carregado a partir do arquivo, ou um catálogo vazio
        ({}) caso o arquivo não exista.
    """
    catalogo = {}
    try:
        with open(caminho, "r", encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                nome, preco, estoque = linha.split(";")
                catalogo[nome] = {"preco": float(preco), "estoque": int(estoque)}
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' não encontrado. Carregando catálogo vazio.")
        return {}
    return catalogo



# ============================================================
# MENUS (implemente aqui)
# ============================================================


def menu_cadastrar_produto(catalogo: dict) -> None:
    """Pede os dados de um produto ao usuário e o cadastra no catálogo.

    Args:
        catalogo: dicionário com os produtos do e-commerce.

    Returns:
        O catálogo atualizado, incluindo o novo produto.
    """
    print('-----------------CADASTRO DE PRODUTO-------------------')
    nome_produto = str(input('Qual nome do produto que deseja cadastrar?'))
    preco = float(input('Qual o preço do produto?'))
    estoque = int(input(f'Qual é a quantidade em estoque do {nome_produto}?'))
    catalogo = cadastrar_produto(catalogo, nome_produto, preco, estoque)
    return catalogo


def menu_atualizar_estoque(catalogo: dict) -> None:
    """Pede o nome do produto e a quantidade e atualiza o estoque.

    Args:
        catalogo: dicionário com os produtos do e-commerce.

    Returns:
        O catálogo atualizado.
    """
    print('-----------------ATUALIZAÇÃO DE ESTOQUE-------------------')
    try:
        nome_produto =  str(input('Qual produto deseja atualizar?'))
        if nome_produto in catalogo:
            quantidade = int(input(f'Qual é a quantidade que deseja adicionar ao estoque de {nome_produto}?'))
            catalogo = atualizar_estoque(catalogo, nome_produto, quantidade)
        else:
            raise Exception(f"aconteceualgo.")
    except Exception as e:
        print(f'Erro: {e}')
    return catalogo



def menu_produtos(catalogo: dict) -> None:
    """Exibe o catálogo de produtos.

    Args:
        catalogo: dicionário com os produtos do e-commerce.

    Returns:
        None.
    """
    print('-----------------CATÁLOGO DE PRODUTOS-------------------')
    try:
        return exibir_catalogo(catalogo)
    except Exception as e:
        print(f'Erro: {e}')



def menu_baixo_estoque(catalogo: dict) -> None:
    """Pede um limite ao usuário e retorna os produtos com estoque abaixo dele.

    Args:
        catalogo: dicionário com os produtos do e-commerce.

    Returns:
        Lista com os nomes dos produtos com estoque abaixo do limite
        informado, ou None se ocorrer um erro na conversão do limite.
    """
    print('-----------------PRODUTOS COM ESTOQUE-------------------')
    try:
        limite = int(input("coloca ae o limite meu compatriota: "))
        produtos_baixo_estoque = listar_produtos_baixo_estoque(catalogo, limite)
        if produtos_baixo_estoque:
                        print("Produtos de estoque baixo")
                        for nome in produtos_baixo_estoque:
                            print(f"- {nome}")      
            
    except Exception as e:
        print(f'Erro: {e}')



def menu_cadastrar_usuario(usuarios: dict) -> None:
    """Pede nome, e-mail e senha ao usuário e chama cadastrar_usuario.

    Args:
        usuarios: dicionário com os usuários cadastrados.

    Returns:
        None.
    """
    print('-----------------CADASTRO DE USUÁRIO-------------------')
    try:
        nome = str(input('Qual é o seu nome?'))
        email = str(input('Qual é o seu e-mail?'))
        senha = str(input('Qual é a sua senha?'))
        usuarios = cadastrar_usuario(usuarios, nome, email, senha)
        print(f'Usuário {nome} cadastrado com sucesso!')
    except Exception as e:
        print(f'Erro: {e}')


def menu_login(usuarios: dict) -> None:
    """Pede e-mail e senha ao usuário, chama fazer_login e informa o resultado.

    Args:
        usuarios: dicionário com os usuários cadastrados.

    Returns:
        O resultado retornado por fazer_login (tupla ou string),
        ou None se ocorrer um erro.
    """
    print('-----------------LOGIN DE USUÁRIO-------------------')
    try:
        email = str(input('Qual é o seu e-mail?'))
        senha = str(input('Qual é a sua senha?'))
        resultado_login = fazer_login(usuarios, email, senha)
        print(resultado_login)
        return resultado_login
    except Exception as e:
        print(f'Erro: {e}')



def menu_salvar_catalogo(catalogo: dict) -> None:
    """Pede um caminho de arquivo ao usuário e salva o catálogo nele.

    Args:
        catalogo: dicionário com os produtos do e-commerce.

    Returns:
        O catálogo, se o caminho informado for considerado válido e o
        salvamento ocorrer; None caso contrário.
    """
    print('-----------------SALVAR CATÁLOGO EM ARQUIVO-------------------')
    try: 
        caminho = str(input( 'Qual é o nome do arquivo que deseja colocar para o catálogo?'))
        salvo = salvar_catalogo_em_arquivo(catalogo, caminho)
        print(f'Catálogo salvo com sucesso como {caminho}!')
        return salvo
    except Exception as e:
        print(f'Erro: {e}')


def menu_carregar_catalogo() -> dict:
    """Pede um caminho de arquivo ao usuário e carrega um catálogo dele.

    Returns:
        O catálogo carregado a partir do arquivo informado.
    """
    print('-----------------CARREGAR CATÁLOGO DE ARQUIVO-------------------')
    caminho = input("Caminho do arquivo para carregar: ")
    catalogo = carregar_catalogo_de_arquivo(caminho)
    print(f"Catálogo carregado de '{caminho}'.")
    return catalogo


def menu_principal(catalogo: dict, usuarios: dict) -> str | dict:
    """Exibe o menu principal e executa a opção escolhida pelo usuário.

    Args:
        catalogo (dict[str, Any]): Dicionário com os produtos do e-commerce.
        usuarios (dict[str, Any]): Dicionário com os usuários cadastrados.

    Returns:
        str | dict[str, Any]: A string "SAIR" se o programa for encerrado, 
        ou o catálogo atualizado nos demais casos.
    """
      
    print("\n================================")
    print("         MEU E-COMMERCE         ")
    print("================================")
    print("1 - Cadastrar produto\n2 - Atualizar estoque\n3 - Ver catálogo")
    print("4 - Produtos com baixo estoque\n5 - Cadastrar usuário\n6 - Fazer login")
    print("7 - Salvar catálogo em arquivo\n8 - Carregar catálogo de arquivo\n0 - Sair")

    opcao = input("Escolha uma opção: ")
        
    opcoes  = {
        "1": (menu_cadastrar_produto, (catalogo,)),
        "2": (menu_atualizar_estoque, (catalogo,)),
        "3": (menu_produtos, (catalogo,)),
        "4": (menu_baixo_estoque, (catalogo,)),
        "5": (menu_cadastrar_usuario, (usuarios,)),
        "6": (menu_login, (usuarios,)),
        "7": (menu_salvar_catalogo, (catalogo,)),
        }

    if opcao == "0":
            return "SAIR"
    if opcao == "8":
            return menu_carregar_catalogo()
    if opcao in opcoes:
            funcao, args = opcoes[opcao]
            funcao(*args)
    else:
            print("opção inválida.")
                
    return catalogo
        

# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":
    # Catálogo inicial de produtos (você pode reaproveitar os dados
    # abaixo ou cadastrar os seus).
    catalogo = {}
    catalogo = cadastrar_produto(catalogo, "Camiseta Azul", 59.90, 120)
    catalogo = cadastrar_produto(catalogo, "Tênis Runner", 199.90, 60)
    catalogo = cadastrar_produto(catalogo, "Boné Preto", 39.90, 50)

    usuarios = {}

    while True:
        resultado = menu_principal(catalogo, usuarios)
        if resultado == "SAIR":
            print("Encerrando o programa. Até mais!")
            break
        catalogo = resultado        

