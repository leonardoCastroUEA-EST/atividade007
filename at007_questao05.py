with open("sistema.log") as f:
    linhas = f.readlines()
sucessos = sum(1 for l in linhas if "Accepted password" in l)
falhas = sum(1 for l in linhas if "Failed password" in l)
print("Sucessos:", sucessos)
print("Falhas:", falhas)
