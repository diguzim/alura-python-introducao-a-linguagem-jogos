import random



def jogar():
    imprime_bem_vindo()

    palavra_secreta = carrega_palavra_secreta()
    # print(palavra_secreta)

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            imprime_tentativas_faltantes(erros)
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print("")
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)
    print("Fim do jogo")


def imprime_bem_vindo():
    print("*********************************")
    print("Bem vindo ao jogo de Forca*******!")
    print("*********************************")


def carrega_palavra_secreta():
    palavras = []
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    return palavras[numero_aleatorio].upper()


def pede_chute():
    chute = input("Digite uma letra: ")
    return chute.strip().upper()


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_tentativas_faltantes(erros):
    print(f"Ops, você errou! Faltam {7 - erros - 1} tentativas.")


def imprime_mensagem_vitoria():
    print("Você venceu!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_derrota(palavra_secreta):
    print("Você perdeu!")
    print(f"A palavra secreta era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
