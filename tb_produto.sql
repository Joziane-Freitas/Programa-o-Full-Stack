-- Criação da tabela Produtos
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,      -- Identificador único para cada produto
    NomeProduto VARCHAR(100),       -- Nome do produto
    Quantidade INT,                 -- Quantidade disponível do produto
    Preco DECIMAL(10, 2)            -- Preço do produto, com duas casas decimais
);

-- Inserção de três registros na tabela Produtos
INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco)
VALUES 
    (1, 'Camiseta', 50, 29.90),    -- Produto 1
    (2, 'Notebook', 20, 2499.99),  -- Produto 2
    (3, 'Mouse', 100, 79.90);      -- Produto 3
