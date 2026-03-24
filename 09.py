# Preço do produto com número decimal
preco = float(input("Digite o preço do produto:"))

# Calcule o valor do desconto
desconto = preco * 10 / 100

# Calcule o novo preço de desconto
preco_final = preco - desconto

# Exibe o preço final
print("Preço com desconto:", preco_final)
