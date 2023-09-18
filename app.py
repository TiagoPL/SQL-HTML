# Crie uma aplicação que permita gerenciar o estoque de uma loja de doces.
from flask import Flask, request    # Utilizado para criar a API.
import sqlite3                      # Utilizado para criar o DB.
import packages.funçoes                      # Arquvo que armazena funções.
import packages.mensagens                    # Arquivo que armazena mensagens de texto.


app = Flask(__name__)

arquivo = open("caixa.txt", "w")
arquivo.close()

# Dá as boas vindas à página inicial da aplicação.
@app.route("/")
def main_page():
    return(f"{packages.mensagens.menu} Bem vindo ao sistema de gerenciamento do estoque!")

# Checa o conteudo atual do banco de dados.
@app.route("/checa_db")
def checa_db():
    # Cria uma conexão com um banco de dados.
    conexao = sqlite3.connect("/db/doces.db")
    cursor = conexao.cursor()
    packages.funçoes.cria_tabela()

    # Cria o comando para checar o conteudo do db.
    comando_checa_tabela = """
    SELECT * FROM doces    
    """

    # Executa o comando.
    cursor.execute(comando_checa_tabela)
    conteudo = cursor.fetchall()
    conexao.close()

    # Cria a string de resposta ao usuario.
    string_do_estoque = ''
    for linha in conteudo:
        string_do_estoque += f"{linha} <br />"

    return f"{packages.mensagens.menu} {string_do_estoque}"

# Adiciona um item na tabela no banco de dados.
@app.route("/adiciona_item")
def adiciona_item():
    try:
        nome = request.args.get("nome")
        preço = float(request.args.get("preço"))
        quantidade = int(request.args.get("quantidade"))

    except ValueError:
        return f"{packages.mensagens.menu} {packages.mensagens.adiciona} Por favor, utilize apenas digitos em 'preço' e 'quantidade'."
    
    except TypeError:
        return f"{packages.mensagens.menu} {packages.mensagens.adiciona}"

    # Cria uma conexão com um banco de dados.
    conexao = sqlite3.connect("/db/doces.db")
    cursor = conexao.cursor()
    packages.funçoes.cria_tabela()

    if nome != None:
        # Cria o comando para adicionar itens à tabela.
        comando_adiciona_item = f"""
        INSERT into doces (nome, preco, quantidade)
        values ("{nome}", "{preço:.2f}", {quantidade})    
        """

        cursor.execute(comando_adiciona_item)
        conexao.commit()
        conexao.close()

        packages.funçoes.log(nome=nome, preço=preço, quantidade=quantidade, ação='adicionado ao')

        return f"{packages.mensagens.menu} {packages.mensagens.adiciona} O item {nome} foi adicionado ao estoque!"

    else:
        return f'{packages.mensagens.menu} {packages.mensagens.adiciona}'

# Remove um item da tabela no banco de dados.
@app.route("/remove_item")
def remove_item():
    try:
        id = int(request.args.get("id"))
    except ValueError:
        return f'{packages.mensagens.menu} {packages.mensagens.remove} Por favor, utilize apenas digitos.'
    except TypeError:
        return f'{packages.mensagens.menu} {packages.mensagens.remove}'

    # Cria uma conexão com um banco de dados.
    conexao = sqlite3.connect("/db/doces.db")
    cursor = conexao.cursor()
    packages.funçoes.cria_tabela()

    # Cria o comando para checar o conteudo do db.
    comando_checa_tabela = """
    SELECT id FROM doces    
    """

    # Executa o comando.
    cursor.execute(comando_checa_tabela)
    conteudo = cursor.fetchall()

    lista = []

    for tupla in conteudo:
        lista.append(tupla[0])
    
    if id in lista:
        # Cria o comando para remover itens da tabela.
        comando_remove_item = f"""
        DELETE from doces WHERE id = "{id}"
        """

        cursor.execute(comando_remove_item)
        conexao.commit()
        conexao.close()

        packages.funçoes.log(id=id, ação='removido do')

        return f'{packages.mensagens.menu} {packages.mensagens.remove} Item removido do estoque.'

    else:
        return f'{packages.mensagens.menu} {packages.mensagens.remove} O ID digitado não existe no estoque.'

# Atualiza um item na tabela no banco de dados.
@app.route("/atualiza_item")
def atualiza_item():
    try:
        id = int(request.args.get("id"))
        quantidade = int(request.args.get("quantidade"))
    except TypeError:
        return f"{packages.mensagens.menu} {packages.mensagens.atualiza}"
    except ValueError:
        return f"{packages.mensagens.menu} {packages.mensagens.atualiza} Por favor utilize apenas digitos nos campos 'id' e 'quantidade'."

    # Cria uma conexão com um banco de dados.
    conexao = sqlite3.connect("/db/doces.db")
    cursor = conexao.cursor()
    packages.funçoes.cria_tabela()

    # Cria o comando para checar o conteudo do db.
    comando_checa_tabela = """
    SELECT id FROM doces    
    """

    # Executa o comando.
    cursor.execute(comando_checa_tabela)
    conteudo = cursor.fetchall()

    lista = []

    for tupla in conteudo:
        lista.append(tupla[0])
    
    if id in lista:
        packages.funçoes.caixa_registradora(id, quantidade)

        # Cria o comando para atualizar um item na tabela.
        comando_atualiza_item = f"""
        UPDATE doces
        SET quantidade = {quantidade}
        WHERE id = "{id}"
        """

        cursor.execute(comando_atualiza_item)
        conexao.commit()
        conexao.close()

        return f"{packages.mensagens.menu} {packages.mensagens.atualiza} O item teve sua quantidade alterada para {quantidade}."

    else:
        return f"{packages.mensagens.menu} {packages.mensagens.atualiza} O ID digitado não existe no estoque."
