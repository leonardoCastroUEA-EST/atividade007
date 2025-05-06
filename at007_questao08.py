import re
from collections import Counter

with open("sistema.log") as f:
    linhas = f.readlines()

usuarios = [re.search(r"Failed password for (\w+)", l).group(1) for l in linhas if "Failed password" in l]
contagem = Counter(usuarios)
for usuario, qtd in contagem.items():
    if qtd > 1:
        print(f"{usuario}: {qtd}")
