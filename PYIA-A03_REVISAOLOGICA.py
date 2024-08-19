produtos = {}

for i in range(2):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_produto = float(input(f"Digite o preço do produto {i+1}: "))
    produtos[nome_produto] = preco_produto

valor_total = sum(produtos.values())

print(f"\nO valor total da compra é: R$ {valor_total:.2f}")
