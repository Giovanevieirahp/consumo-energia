#entrada de dados
nome_aparelho = input("Insira o nome do aparelho: ")
potencia_aparelho = float(input("Informe a potência do aparelho (W): "))
uso_diario = float(input("Informe o uso diário do aparelho (horas): "))
#processamento
consumoMensal = (potencia_aparelho * uso_diario * 30) / 1000
custoMensal = consumoMensal * 0.75
#saida de dados (sepada por linhas)
print(f"Aparelho: {nome_aparelho}")
print(f"custo estimado: {consumoMensal:.2f} kWh")
print(f"custo estimado: R${custoMensal:.2f}")