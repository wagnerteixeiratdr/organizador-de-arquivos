import os
import shutil

pasta_origem = "bagunça"

if not os.path.exists(pasta_origem):
    print("A pasta não existe.")
    exit()

arquivos = os.listdir(pasta_origem)

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta_origem, arquivo)

    if os.path.isdir(caminho_completo):
        continue

    _, extensao = os.path.splitext(arquivo)
    extensao = extensao[1:].upper()

    if not extensao:
        extensao = "OUTROS"

    pasta_destino = os.path.join(pasta_origem, extensao)

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    novo_caminho = os.path.join(pasta_destino, arquivo)
    shutil.move(caminho_completo, novo_caminho)

print("Arquivos organizados com sucesso!")
