-- Criando tabela produtos e vendas
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    quantidade_disponivel INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade_vendida INT NOT NULL,
    data_venda DATETIME NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
