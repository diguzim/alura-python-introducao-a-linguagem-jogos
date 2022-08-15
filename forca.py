import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca*******!")
    print("*********************************")

    palavras = []
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()

    print(palavra_secreta)

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
