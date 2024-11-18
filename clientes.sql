CREATE TABLE `clientes` (
  `id_Clientes` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(80) NOT NULL,
  `idade` int NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `Clientescol` varchar(45) NOT NULL,
  PRIMARY KEY (`id_Clientes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci