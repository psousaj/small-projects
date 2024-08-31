"""
Escreva um programa na linguagem que desejar 
onde calcule o percentual de representação que 
cada estado teve dentro do valor total mensal da distribuidora.
"""

SP = {"valor": 6783643, "percentual": 0.0}
RJ = {"valor": 3667866, "percentual": 0.0}
MG = {"valor": 2922988, "percentual": 0.0}
ES = {"valor": 2716548, "percentual": 0.0}
OUTROS = {"valor": 1984953, "percentual": 0.0}

valor_total = SP["valor"] + RJ["valor"] + MG["valor"] + ES["valor"] + OUTROS["valor"]

estados = [("SP", SP), ("RJ", RJ), ("MG", MG), ("ES", ES), ("OUTROS", OUTROS)]

for nome, estado in estados:
    valor = estado["valor"]
    estado["percentual"] = (valor / valor_total) * 100

print("Percentual de cada estado: \n")
for nome, estado in estados:
    print(f"{nome}: {estado['percentual']:.1f}%")
