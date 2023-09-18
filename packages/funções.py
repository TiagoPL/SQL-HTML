import sqlite3
import time

def cria_tabela():
    # Cria uma conexão com um banco de dados.
    conexao = sqlite3.connect("doces.db")
    cursor = conexao.cursor()

    # Cria um comando para criar uma tabela no banco de dados.
    comando_cria_tabela = """
    CREATE TABLE doces (
    id integer primary key autoincrement,
    nome text,
    preco,
    quantidade integer
    )      
    """
    
    # Tenta executar o comando criado, salvar as alterações e fecha a conexão.
    try:
        cursor.execute(comando_cria_tabela)
        conexao.commit()
    except sqlite3.OperationalError:
        pass

# Mantém um log de entrada/saida do estoque.
def log(id='', nome='', preço='', quantidade='', ação=''):
    horario_maquina = time.time()
    horario_humano = time.localtime(horario_maquina)

    hora = horario_humano.tm_hour
    minuto = horario_humano.tm_min
    segundo = horario_humano.tm_sec

    horario_atual = f"{hora}:{minuto}:{segundo}"

    with open("log.txt", "a+") as arquivo:
        if ação == "adicionado ao":
            arquivo.write(f"{horario_atual} - O item [{nome, preço, quantidade}] foi {ação} banco de dados. \n")
        else:
            arquivo.write(f"{horario_atual} - O item de ID {id} foi {ação} banco de dados. \n")

# Mantém o valor em caixa atual da loja.
def caixa_registradora(id, quantidade):
    # Cria uma conexão com um banco de dados.
    conexao = sqlite3.connect("doces.db")
    cursor = conexao.cursor()

    # Cria o comando para checar o conteudo do db.
    comando_checa_tabela = f"""
    SELECT * FROM doces
    WHERE id = {id}    
    """

    # Executa o comando.
    cursor.execute(comando_checa_tabela)
    conteudo = cursor.fetchall()
    conexao.close()

    valor = 0
    if int(quantidade) < int(conteudo[0][3]):
        valor += ((int(conteudo[0][3]) - int(quantidade)) * float(conteudo[0][2]))

    arquivo = open("caixa.txt", "r")
    conteudo = arquivo.readlines()
    arquivo.close()

    print(conteudo)

    arquivo = open("caixa.txt", "w")
    try:
        arquivo.write(f"{float(conteudo[0]) + valor}")
    except IndexError:
        arquivo.write(f"{valor}")
    arquivo.close()
