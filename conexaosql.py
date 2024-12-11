import pymysql.cursors

# Conectar ao banco de dados
connection = pymysql.connect(host='localhost',
                             user='usuario',
                             password='senha',
                             database='loja',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Exemplo de cadastro de um novo produto
        sql = "INSERT INTO `Produtos` (`Nome`, `Descricao`, `QuantidadeDisponivel`, `Preco`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, ('Produto A', 'Descrição do Produto A', 100, 29.99))

    connection.commit()

    with connection.cursor() as cursor:
        # Exemplo de consulta de produtos
        sql = "SELECT * FROM `Produtos`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()

# POO

class Produto:
    def __init__(self, produto_id, nome, descricao, quantidade_disponivel, preco):
        self.produto_id = produto_id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

class Venda:
    def __init__(self, venda_id, produto_id, quantidade_vendida, data_venda):
        self.venda_id = venda_id
        self.produto_id = produto_id
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = data_venda

#integrando banco de dados com POO

class Estoque:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='usuario',
                                          password='senha',
                                          database='loja',
                                          cursorclass=pymysql.cursors.DictCursor)

    def cadastrar_produto(self, nome, descricao, quantidade_disponivel, preco):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `Produtos` (`Nome`, `Descricao`, `QuantidadeDisponivel`, `Preco`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nome, descricao, quantidade_disponivel, preco))
        self.connection.commit()

    def consultar_produtos(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM `Produtos`"
            cursor.execute(sql)
            return cursor.fetchall()

    def atualizar_quantidade(self, produto_id, quantidade_disponivel):
        with self.connection.cursor() as cursor:
            sql = "UPDATE `Produtos` SET `QuantidadeDisponivel` = %s WHERE `ProdutoID` = %s"
            cursor.execute(sql, (quantidade_disponivel, produto_id))
        self.connection.commit()

    def remover_produto(self, produto_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `Produtos` WHERE `ProdutoID` = %s"
            cursor.execute(sql, (produto_id,))
        self.connection.commit()

# Exemplo de uso
estoque = Estoque()
estoque.cadastrar_produto('Produto A', 'Descrição do Produto A', 100, 29.99)
produtos = estoque.consultar_produtos()
print(produtos)


