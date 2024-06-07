import datetime
import uuid

# Função para validar entrada do usuário
def validar_entrada(prompt, tipo):
    while True:
        entrada = input(prompt)
        if tipo == 'int':
            if entrada.isdigit():
                return int(entrada)
            else:
                print("Entrada inválida. Digite um número inteiro.")
        elif tipo == 'float':
            try:
                return float(entrada)
            except ValueError:
                print("Entrada inválida. Digite um número decimal.")
        elif tipo == 'data':
            try:
                if len(entrada) == 8 and entrada.isdigit():
                    entrada_formatada = f"{entrada[:2]}/{entrada[2:4]}/{entrada[4:]}"
                    return datetime.datetime.strptime(entrada_formatada, "%d/%m/%Y")
                else:
                    print("Entrada inválida. Digite a data no formato DDMMYYYY.")
            except ValueError:
                print("Entrada inválida. Digite a data no formato DDMMYYYY.")
        else:
            return entrada

# Funções para manipulação das entidades
def adicionar_usuario(usuarios):
    usuario_id = str(uuid.uuid4())
    nome = validar_entrada("Nome: ", 'str')
    email = validar_entrada("Email: ", 'str')
    data_cadastro = validar_entrada("Data de Cadastro (DDMMYYYY): ", 'data')
    usuarios.append({
        'usuario_id': usuario_id,
        'nome': nome,
        'email': email,
        'data_cadastro': data_cadastro
    })

def adicionar_conteudo(conteudos, usuario_id):
    conteudo_id = str(uuid.uuid4())
    titulo = validar_entrada("Título: ", 'str')
    descricao = validar_entrada("Descrição: ", 'str')
    data_publicacao = validar_entrada("Data de Publicação (DDMMYYYY): ", 'data')
    conteudos.append({
        'conteudo_id': conteudo_id,
        'usuario_id': usuario_id,
        'titulo': titulo,
        'descricao': descricao,
        'data_publicacao': data_publicacao
    })

def adicionar_evento(eventos):
    evento_id = str(uuid.uuid4())
    localizacao = validar_entrada("Localização: ", 'str')
    data_evento = validar_entrada("Data do Evento (DDMMYYYY): ", 'data')
    descricao = validar_entrada("Descrição: ", 'str')
    eventos.append({
        'evento_id': evento_id,
        'localizacao': localizacao,
        'data_evento': data_evento,
        'descricao': descricao
    })

def adicionar_dados_poluicao(dados_poluicao):
    dados_id = str(uuid.uuid4())
    localizacao = validar_entrada("Localização: ", 'str')
    quantidade_lixo = validar_entrada("Quantidade de Lixo (kg): ", 'float')
    data_coleta = validar_entrada("Data da Coleta (DDMMYYYY): ", 'data')
    dados_poluicao.append({
        'dados_id': dados_id,
        'localizacao': localizacao,
        'quantidade_lixo': quantidade_lixo,
        'data_coleta': data_coleta
    })

def adicionar_recurso_marinhos(recursos_marinhos):
    recurso_id = str(uuid.uuid4())
    nome = validar_entrada("Nome do Recurso: ", 'str')
    tipo = validar_entrada("Tipo de Recurso (peixes, algas, corais, etc.): ", 'str')
    descricao = validar_entrada("Descrição: ", 'str')
    recursos_marinhos.append({
        'recurso_id': recurso_id,
        'nome': nome,
        'tipo': tipo,
        'descricao': descricao
    })

def adicionar_doacao(doacoes, usuario_id):
    doacao_id = str(uuid.uuid4())
    valor = validar_entrada("Valor da Doação: ", 'float')
    data_doacao = validar_entrada("Data da Doação (DDMMYYYY): ", 'data')
    forma_pagamento = validar_entrada("Forma de Pagamento (cheque, dinheiro, cartão de crédito): ", 'str')
    doacoes.append({
        'doacao_id': doacao_id,
        'usuario_id': usuario_id,
        'valor': valor,
        'data_doacao': data_doacao,
        'forma_pagamento': forma_pagamento
    })


#listar dados cadastrados pelo usuario
def listar_dados_cadastrados(usuarios, conteudos, eventos, dados_poluicao, recursos_marinhos, doacoes):
    print("\nDados Cadastrados:")
    print("\nUsuários:")
    for usuario in usuarios:
        print("ID:", usuario['usuario_id'])
        print("Nome:", usuario['nome'])
        print("Email:", usuario['email'])
        print("Data de Cadastro:", usuario['data_cadastro'].strftime("%d/%m/%Y"))
        print("---------------------------")

    print("\nConteúdos:")
    for conteudo in conteudos:
        print("ID do Conteúdo:", conteudo['conteudo_id'])
        print("Título:", conteudo['titulo'])
        print("Descrição:", conteudo['descricao'])
        print("Data de Publicação:", conteudo['data_publicacao'].strftime("%d/%m/%Y"))
        print("ID do Usuário:", conteudo['usuario_id'])
        print("---------------------------")

    print("\nEventos de Limpeza:")
    for evento in eventos:
        print("ID do Evento:", evento['evento_id'])
        print("Localização:", evento['localizacao'])
        print("Data do Evento:", evento['data_evento'].strftime("%d/%m/%Y"))
        print("Descrição:", evento['descricao'])
        print("---------------------------")

    print("\nDados de Poluição:")
    for dado in dados_poluicao:
        print("ID do Dado:", dado['dados_id'])
        print("Localização:", dado['localizacao'])
        print("Quantidade de Lixo (kg):", dado['quantidade_lixo'])
        print("Data da Coleta:", dado['data_coleta'].strftime("%d/%m/%Y"))
        print("---------------------------")

    print("\nRecursos Marinhos:")
    for recurso in recursos_marinhos:
        print("ID do Recurso:", recurso['recurso_id'])
        print("Nome:", recurso['nome'])
        print("Tipo:", recurso['tipo'])
        print("Descrição:", recurso['descricao'])
        print("---------------------------")

    print("\nDoações:")
    for doacao in doacoes:
        print("ID da Doação:", doacao['doacao_id'])
        print("ID do Usuário:", doacao['usuario_id'])
        print("Valor:", doacao['valor'])
        print("Data da Doação:", doacao['data_doacao'].strftime("%d/%m/%Y"))
        print("Forma de Pagamento:", doacao['forma_pagamento'])
        print("---------------------------")

# Função para o submenu de opções de conteúdo
def submenu_conteudo(conteudos, usuarios):
    while True:
        print("\nSubmenu de Conteúdo")
        print("1. Adicionar Conteúdo")
        print("2. Listar Conteúdos")
        print("3. Voltar ao Menu Principal")

        escolha = validar_entrada("Escolha uma opção: ", 'int')

        if escolha == 1:
            usuario_id = validar_entrada("ID do Usuário: ", 'str')
            adicionar_conteudo(conteudos, usuario_id)
            print("Conteúdo adicionado com sucesso!")

        elif escolha == 2:
            print("\nLista de Conteúdos:")
            for conteudo in conteudos:
                print("ID:", conteudo['conteudo_id'])
                print("Título:", conteudo['titulo'])
                print("Descrição:", conteudo['descricao'])
                print("Data de Publicação:", conteudo['data_publicacao'].strftime("%d/%m/%Y"))
                print("---------------------------")

        elif escolha == 3:
            break

        else:
            print("Opção inválida. Tente novamente.")

# Função para o submenu de opções de evento de limpeza
def submenu_evento(eventos):
    while True:
        print("\nSubmenu de Evento de Limpeza")
        print("1. Adicionar Evento de Limpeza")
        print("2. Listar Eventos de Limpeza")
        print("3. Voltar ao Menu Principal")

        escolha = validar_entrada("Escolha uma opção: ", 'int')

        if escolha == 1:
            adicionar_evento(eventos)
            print("Evento de Limpeza adicionado com sucesso!")

        elif escolha == 2:
            print("\nLista de Eventos de Limpeza:")
            for evento in eventos:
                print("ID:", evento['evento_id'])
                print("Localização:", evento['localizacao'])
                print("Data do Evento:", evento['data_evento'].strftime("%d/%m/%Y"))
                print("Descrição:", evento['descricao'])
                print("---------------------------")

        elif escolha == 3:
            break

        else:
            print("Opção inválida. Tente novamente.")

# Função principal do sistema
def main():
    usuarios = []
    conteudos = []
    eventos = []
    dados_poluicao = []
    recursos_marinhos = []
    doacoes = []

    while True:
        print("\nMenu Principal")
        print("1. Adicionar Usuário")
        print("2. Submenu de Conteúdo")
        print("3. Submenu de Evento de Limpeza")
        print("4. Adicionar Dados de Poluição")
        print("5. Adicionar Recurso Marinho")
        print("6. Adicionar Doação")
        print("7. Listar dados cadastrados")
        print("8. Sair do sistema")

        escolha = validar_entrada("Escolha uma opção: ", 'int')

        if escolha == 1:
            adicionar_usuario(usuarios)
            print("Usuário adicionado com sucesso!")

        elif escolha == 2:
            submenu_conteudo(conteudos, usuarios)

        elif escolha == 3:
            submenu_evento(eventos)

        elif escolha == 4:
            adicionar_dados_poluicao(dados_poluicao)
            print("Dados de Poluição adicionados com sucesso!")

        elif escolha == 5:
            adicionar_recurso_marinhos(recursos_marinhos)

        elif escolha == 6:
            adicionar_doacao(doacoes)

        elif escolha == 7:
            listar_dados_cadastrados(usuarios, conteudos, eventos, dados_poluicao)

        elif escolha == 8:
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema
if __name__ == "__main__":
    main()
