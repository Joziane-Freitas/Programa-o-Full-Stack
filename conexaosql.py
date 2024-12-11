#Estutura de classes (POO)

class Produto:
    def __init__(self, id, nome, descricao, quantidade_disponivel, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

    def atualizar_quantidade(self, quantidade):
        self.quantidade_disponivel += quantidade
    
    def __str__(self):
        return f"Produto(ID: {self.id}, Nome: {self.nome}, Quantidade: {self.quantidade_disponivel}, Preço: R${self.preco})"

# Classe venda

import datetime

class Venda:
    def __init__(self, id, produto, quantidade_vendida, data_venda=None):
        self.id = id
        self.produto = produto  # Objeto Produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda if data_venda else datetime.datetime.now()

    def __str__(self):
        return f"Venda(ID: {self.id}, Produto: {self.produto.nome}, Quantidade: {self.quantidade_vendida}, Data: {self.data_venda})"

# Funções Create, Read, Update, Delete

import mysql.connector

def cadastrar_produto(produto):
    conn = mysql.connector.connect(user='root', password='sua_senha', host='localhost', database='estoque')
    cursor = conn.cursor()

    query = "INSERT INTO produtos (nome, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)"
    data = (produto.nome, produto.descricao, produto.quantidade_disponivel, produto.preco)
    
    cursor.execute(query, data)
    conn.commit()
    
    cursor.close()
    conn.close()

    print(f"Produto {produto.nome} cadastrado com sucesso!")

# Função para consultar produto

def consultar_produto(id_produto):
    conn = mysql.connector.connect(user='root', password='sua_senha', host='localhost', database='estoque')
    cursor = conn.cursor()

    query = "SELECT * FROM produtos WHERE id = %s"
    cursor.execute(query, (id_produto,))
    
    resultado = cursor.fetchone()
    if resultado:
        produto = Produto(*resultado)
        print(produto)
    else:
        print(f"Produto com ID {id_produto} não encontrado.")
    
    cursor.close()
    conn.close()
 
 # Função Atualizar quantidade de produto
 
def atualizar_quantidade_produto(id_produto, quantidade):
    conn = mysql.connector.connect(user='root', password='sua_senha', host='localhost', database='estoque')
    cursor = conn.cursor()

    query = "UPDATE produtos SET quantidade_disponivel = quantidade_disponivel + %s WHERE id = %s"
    cursor.execute(query, (quantidade, id_produto))
    conn.commit()

    cursor.close()
    conn.close()

    print(f"Quantidade do produto ID {id_produto} atualizada com sucesso!")


# Função para deletar produto

def remover_produto(id_produto):
    conn = mysql.connector.connect(user='root', password='sua_senha', host='localhost', database='estoque')
    cursor = conn.cursor()

    query = "DELETE FROM produtos WHERE id = %s"
    cursor.execute(query, (id_produto,))
    conn.commit()

    cursor.close()
    conn.close()

    print(f"Produto ID {id_produto} removido com sucesso!")

# Função para Registrar Venda

def registrar_venda(venda):
    conn = mysql.connector.connect(user='root', password='sua_senha', host='localhost', database='estoque')
    cursor = conn.cursor()

    query = "INSERT INTO vendas (produto_id, quantidade_vendida, data_venda) VALUES (%s, %s, %s)"
    data = (venda.produto.id, venda.quantidade_vendida, venda.data_venda)
    
    cursor.execute(query, data)
    conn.commit()

    # Atualizando a quantidade do produto
    venda.produto.atualizar_quantidade(-venda.quantidade_vendida)
    atualizar_quantidade_produto(venda.produto.id, -venda.quantidade_vendida)

    cursor.close()
    conn.close()

    print(f"Venda de {venda.quantidade_vendida} unidades de {venda.produto.nome} registrada com sucesso!")
