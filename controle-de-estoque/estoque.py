# Controle de Estoque e Vendas
# Trabalho de lógica de programação / banco de dados
# Sistema pra cadastrar produto, ver estoque e registrar venda

import sqlite3
from datetime import datetime

banco = sqlite3.connect("estoque.db")
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    quantidade INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    quantidade INTEGER,
    total REAL,
    data TEXT
)
""")
banco.commit()

ESTOQUE_MINIMO = 5


def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preco (ex 19.90): ").replace(",", "."))
    qtd = int(input("Quantidade: "))

    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?,?,?)", (nome, preco, qtd))
    banco.commit()
    print("Produto cadastrado!")


def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if len(produtos) == 0:
        print("nenhum produto cadastrado")
        return

    for p in produtos:
        aviso = ""
        if p[3] <= ESTOQUE_MINIMO:
            aviso = " (estoque baixo!!)"
        print(str(p[0]) + " - " + p[1] + " - R$" + str(p[2]) + " - qtd: " + str(p[3]) + aviso)


def vender():
    listar_produtos()
    produto_id = input("\nId do produto vendido: ")
    qtd_vendida = int(input("Quantidade: "))

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    if produto == None:
        print("produto nao encontrado")
        return

    if qtd_vendida > produto[3]:
        print("nao tem estoque suficiente, so tem " + str(produto[3]))
        return

    total = qtd_vendida * produto[2]
    nova_qtd = produto[3] - qtd_vendida

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, produto_id))
    data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("INSERT INTO vendas (produto_id, quantidade, total, data) VALUES (?,?,?,?)",
                   (produto_id, qtd_vendida, total, data_hoje))
    banco.commit()

    print("Venda feita! Total: R$" + str(total))
    if nova_qtd <= ESTOQUE_MINIMO:
        print("atencao, estoque desse produto ta ficando baixo")


def historico():
    cursor.execute("""
        SELECT vendas.id, produtos.nome, vendas.quantidade, vendas.total, vendas.data
        FROM vendas, produtos
        WHERE vendas.produto_id = produtos.id
    """)
    vendas = cursor.fetchall()

    if len(vendas) == 0:
        print("nenhuma venda ainda")
        return

    total_geral = 0
    for v in vendas:
        print(str(v[0]) + " - " + v[4] + " - " + v[1] + " - qtd " + str(v[2]) + " - R$" + str(v[3]))
        total_geral = total_geral + v[3]

    print("\ntotal vendido: R$" + str(total_geral))


while True:
    print("\n----- CONTROLE DE ESTOQUE -----")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender")
    print("4 - Historico de vendas")
    print("5 - Sair")

    opcao = input("Escolhe uma opcao: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        vender()
    elif opcao == "4":
        historico()
    elif opcao == "5":
        print("saindo...")
        break
    else:
        print("opcao invalida")

banco.close()
