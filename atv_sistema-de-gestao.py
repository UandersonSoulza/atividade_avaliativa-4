# Lista para armazenar os livros, cada livro será um dicionário
biblioteca = []

# Funções para as funcionalidades do sistema

def cadastrar_livro():
    """Adiciona um novo livro a biblioteca."""
    print("\n--- Cadastrar Novo Livro ---")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    codigo = input("Digite o Código do livro: ") # Identificador único do livro

    # Verifica se já existe um livro com o mesmo Código para evitar duplicatas
    for livro in biblioteca:
        if livro['codigo'] == codigo:
            print(f"Erro: Já existe um livro cadastrado com o Código {codigo}.")
            return # Sai da função se o código já existir

    novo_livro = {
        'titulo': titulo,
        'autor': autor,
        'codigo': codigo,
        'status': 'Disponível' # Status inicial do livro
    }
    biblioteca.append(novo_livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    """Lista todos os livros cadastrados."""
    print("\n--- Lista de Todos os Livros ---")
    if not biblioteca:
        print("Nenhum livro cadastrado no momento.")
        return

    for i, livro in enumerate(biblioteca):
        print(f"\nLivro #{i+1}:")
        print(f"  Título: {livro['titulo']}")
        print(f"  Autor: {livro['autor']}")
        print(f"  Código: {livro['codigo']}")
        print(f"  Status: {livro['status']}")
    print("-" * 20)

def buscar_livro_por_titulo():
    """Busca livros com título que a palavra-chave foi informada"""
    print("\n Buscar Livro por Título ")
    if not biblioteca:
        print("Nenhum livro cadastrado")
        return

    termo_busca = input("Digite o termo para buscar no título: ").lower()
    livros_encontrados = []

    for livro in biblioteca:
        if termo_busca in livro['titulo'].lower():
            livros_encontrados.append(livro)

    if not livros_encontrados:
        print(f"Nenhum livro encontrado com o termo '{termo_busca}' no título.")
    else:
        print(f"\n--- Livros Encontrados com '{termo_busca}' ---")
        for i, livro in enumerate(livros_encontrados):
            print(f"\nLivro Encontrado #{i+1}:")
            print(f"  Título: {livro['titulo']}")
            print(f"  Autor: {livro['autor']}")
            print(f"  Código: {livro['codigo']}")
            print(f"  Status: {livro['status']}")
        print("-" * 20)

def alterar_status_livro():
    """Altera o status de um livro (Emprestado/Disponível) buscando pelo Código."""
    print("\n--- Alterar Status do Livro ---")
    if not biblioteca:
        print("Nenhum livro cadastrado para alterar o status.")
        return

    codigo_busca = input("Digite o Código do livro que deseja alterar o status: ")
    livro_encontrado = None
    indice_livro = -1

    for i, livro in enumerate(biblioteca):
        if livro['codigo'] == codigo_busca:
            livro_encontrado = livro
            indice_livro = i
            break

    if livro_encontrado is None:
        print(f"Nenhum livro encontrado com o Código '{codigo_busca}'.")
    else:
        print(f"\nLivro Encontrado: {livro_encontrado['titulo']} (Status atual: {livro_encontrado['status']})")
        print("Escolha o novo status:")
        print("1. Emprestado")
        print("2. Disponível")
        
        while True:
            escolha_status = input("Digite a opção (1 ou 2): ")
            if escolha_status == '1':
                novo_status = 'Emprestado'
                break
            elif escolha_status == '2':
                novo_status = 'Disponível'
                break
            else:
                print("Opção inválida. Por favor, digite 1 para Emprestado ou 2 para Disponível.")
        
        biblioteca[indice_livro]['status'] = novo_status
        print(f"Status do livro '{livro_encontrado['titulo']}' alterado para '{novo_status}' com sucesso!")

# Menu principal do sistema 
def exibir_menu():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        print("\n--- Sistema de Gestão de Biblioteca ---")
        print("1. Cadastrar")
        print("2. Status Livros")
        print("3. Buscar Livro")
        print("4. Alterar Livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro_por_titulo()
        elif opcao == '4':
            alterar_status_livro()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("inválida.")

#Execução principal do sistema
if __name__ == "__main__":
    exibir_menu()