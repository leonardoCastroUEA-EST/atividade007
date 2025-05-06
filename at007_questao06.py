import re
with open("sistema.log") as f:
    for linha in f:
        if "sudo" in linha:
            match = re.search(r'sudo\[\d+\]: (\w+)', linha)
            if match:
                print(match.group(1))
