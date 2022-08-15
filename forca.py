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

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota()
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
    print(f"Ops, você errou! Faltam {6 - erros - 1} tentativas.")


def imprime_mensagem_vitoria():
    print("Você venceu!")


def imprime_mensagem_derrota():
    print("Você perdeu!")

if __name__ == "__main__":
    jogar()
