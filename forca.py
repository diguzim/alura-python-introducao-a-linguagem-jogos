def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca*******!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        posicao = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                letras_acertadas[posicao] = letra
            posicao += 1

        print(letras_acertadas)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
