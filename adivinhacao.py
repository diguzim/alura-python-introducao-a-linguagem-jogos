print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!\n")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto  # Não utilizado

    if acertou:
        print("Você acertou!\n")
        break
    elif maior:
        print("Você errou! O seu chute foi maior do que o número secreto.\n")
    else:
        print("Você errou! O seu chute foi menor do que o número secreto.\n")

print("Fim do jogo")
