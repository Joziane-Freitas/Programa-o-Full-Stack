-- Criação tabela estoque
CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT,
    DataEntrada DATE,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

-- Combinar informações usando FULL OUTER JOIN

SELECT *
FROM Estoque
FULL OUTER JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID
FULL OUTER JOIN Fornecedores ON Estoque.FornecedorID = Fornecedores.FornecedorID;

-- Agrupar dados com GROUP BY

SELECT FornecedorID, SUM(Quantidade) AS TotalQuantidade
FROM Estoque
GROUP BY FornecedorID;

-- Modificar a estrutura da tabela com ALTER TABLE

ALTER TABLE Estoque
ADD COLUMN Preco DECIMAL(10, 2);

