import re
with open("sistema.log") as f:
    for linha in f:
        if "sshd" in linha and "from" in linha:
            match = re.search(r'from ([\d\.]+)', linha)
            if match:
                print(match.group(1))
