with open("sistema.log") as f:
    for linha in f:
        if "Accepted password" in linha:
            print(linha.strip())
