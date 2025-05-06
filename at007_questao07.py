import re
from datetime import datetime

def extrair_data(linha):
    match = re.match(r"(\w{3} \d{2}) (\d{2}:\d{2}:\d{2})", linha)
    if match:
        return datetime.strptime(match.group(1) + " " + match.group(2), "%b %d %H:%M:%S")
    return datetime.min

with open("sistema.log") as f:
    linhas = [linha.strip() for linha in f]
ordenado = sorted(linhas, key=extrair_data)
for linha in ordenado:
    print(linha)
