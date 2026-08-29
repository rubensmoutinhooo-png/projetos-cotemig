# Agenda de Contatos
# Trabalho de lógica de programação / banco de dados
# Sistema simples pra cadastrar, listar, buscar, editar e apagar contatos

import sqlite3

banco = sqlite3.connect("contatos.db")
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    email TEXT,
    categoria TEXT
)
""")
banco.commit()


def cadastrar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    categoria = input("Categoria (familia, trabalho, amigo...): ")

    cursor.execute("INSERT INTO contatos (nome, telefone, email, categoria) VALUES (?,?,?,?)",
                   (nome, telefone, email, categoria))
    banco.commit()
    print("Contato cadastrado!")


def listar():
    cursor.execute("SELECT * FROM contatos")
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print("Não tem nenhum contato ainda")
        return

    for c in resultado:
        print(str(c[0]) + " - " + c[1] + " - tel: " + str(c[2]) + " - email: " + str(c[3]) + " - " + str(c[4]))


def buscar():
    nome = input("Digite o nome pra buscar: ")
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',))
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print("não achei ninguém com esse nome")
        return

    for c in resultado:
        print(str(c[0]) + " - " + c[1] + " - tel: " + str(c[2]) + " - email: " + str(c[3]))


def editar():
    listar()
    id_contato = input("\nDigite o id do contato que quer editar: ")

    cursor.execute("SELECT * FROM contatos WHERE id = ?", (id_contato,))
    contato = cursor.fetchone()

    if contato == None:
        print("id nao encontrado")
        return

    print("aperta enter se nao quiser mudar")
    novo_nome = input("Nome (" + contato[1] + "): ")
    novo_tel = input("Telefone (" + str(contato[2]) + "): ")
    novo_email = input("Email (" + str(contato[3]) + "): ")

    if novo_nome == "":
        novo_nome = contato[1]
    if novo_tel == "":
        novo_tel = contato[2]
    if novo_email == "":
        novo_email = contato[3]

    cursor.execute("UPDATE contatos SET nome=?, telefone=?, email=? WHERE id=?",
                   (novo_nome, novo_tel, novo_email, id_contato))
    banco.commit()
    print("editado com sucesso")


def apagar():
    listar()
    id_contato = input("\nDigite o id do contato que quer apagar: ")
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    banco.commit()
    print("contato apagado")


# menu principal
while True:
    print("\n----- AGENDA DE CONTATOS -----")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Editar")
    print("5 - Apagar")
    print("6 - Sair")

    opcao = input("Escolhe uma opcao: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        editar()
    elif opcao == "5":
        apagar()
    elif opcao == "6":
        print("saindo...")
        break
    else:
        print("opcao invalida")

banco.close()
