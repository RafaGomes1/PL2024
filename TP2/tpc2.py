import re, sys

def converte(texto):
    # Cabeçalho
    texto = re.sub(r"^# (.*)$", r"<h1>\1</h1>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^## (.*)$", r"<h2>\1</h2>", texto, flags=re.MULTILINE)
    texto = re.sub(r"^### (.*)$", r"<h3>\1</h3>", texto, flags=re.MULTILINE)


    # Bold
    texto = re.sub(r"\*\*(.*)\*\*", r"<b>\1</b>", texto, flags=re.MULTILINE)

    # Italic
    texto = re.sub(r"\*(.*)\*", r"<i>\1</i>", texto, flags=re.MULTILINE)

    texto = re.sub(r"\[(.*)\]\((.*)\)", r'<a href="\2">\1</a>', texto, flags=re.MULTILINE)

    # Imagens
    texto = re.sub(r"!\[(.*)\]\((.*)\)", r'<img src="\2" alt="\1">', texto, flags=re.MULTILINE)







    return texto
    

def main():
    if (len(sys.argv)) > 1:
        with open(sys.argv[1]) as f:
            texto = f.read()
        
        html = converte(texto)
        print(html)

        with open("texto.html", "w") as resultado:
            resultado.write(html)

    else:
        print("Error")

main()




