from functools import reduce
import json

"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""

with open("desafio3.json", "r") as file:
    data = json.load(file)

faturamento_filtrado = []
for faturamento in data["faturamento_diario"]:
    if faturamento["valor"] != 0.0:
        faturamento_filtrado.append(faturamento["valor"])

soma = reduce(lambda acumulador, x: acumulador + x, faturamento_filtrado)
# soma  = sum(faturamento_filtrado) ##Ou algo mais simples
menor_valor = min(faturamento_filtrado)
maior_valor = max(faturamento_filtrado)

media = soma / len(faturamento_filtrado)

dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media)

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
