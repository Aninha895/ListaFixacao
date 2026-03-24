# Le a quantidade de minutos
minutos = int(input("Digite a quantidade de minutos:"))

# Calcule a quantidade de horas interas
horas = minutos // 60

# Calcule o minutos que sobraram
minutos_restantes = minutos % 60

# Exibe o resultado no formato pedido
print(horas, "h", minutos_restantes, "min")