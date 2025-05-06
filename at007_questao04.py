with open("sistema.log") as f:
    for linha in f:
        if "Failed password" in linha:
            print(linha.strip())
