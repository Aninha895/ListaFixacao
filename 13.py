# Le o salario atual
salario = float(input("Digite o salario:"))

# Le o percentual do aumento
percentual = float(input("Digite percentual do aumeto:"))

# Calcule o valor do aumento
aumento = salario * percentual / 100

# Calcule o novo salario
novo_salario = salario + aumento

# Exibe o novo salario
print("Novo salario:", novo_salario)
