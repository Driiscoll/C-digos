import os

caminho = "C:\\Users\\Italo\\OneDrive\\Documentos\\Pessoal\\comandos e anotações\\git comandos.txt"
try:
    with open(caminho) as arquivo:

        if os.path.exists(caminho):
            print("esse local existe")
            if os.path.isfile(caminho):
                print("Isso é um arquivo")
                print(arquivo.read())
            elif os.path.isdir(caminho):
                print("isso é uma pasta")
        else:
            print("esse local não existe")
except Exception as e:
    print(e)