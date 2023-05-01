from funcoes import clean
clean()
reiniciar = True
while reiniciar:
    print(" ### Bem vindo ao jogo da forca ### ")
    nomeJogador = input("\nInsira seu nome de jogador: ")
    nomeDesafiante = input("\nInsira seu nome de desafiante: ")

    clean()

    palavraChave = input("\nPalavra dessa rodada: ")
    dica1 = input("Primeira dica: ")
    dica2 = input("Segunda dica: ")
    dica3 = input("Terceira dica: ")
    clean()

    print("\nA palavra contem:",(len(palavraChave)),"letras")
    for i in range(len(palavraChave)):
        print("_", end="")
    dicas = 0
    tentativas = 0
    chances = 5
    letras = []
    perdeu = False
    ganhou = False
    palavra = ["_"] * len(palavraChave)
    print("\n")    
    while tentativas < chances and "".join(palavra) != palavraChave:
        jogar_ou_pedir_dica = input("\nSelecione: (1) para 'jogar' ou (2) para 'pedir dica': ")
        if jogar_ou_pedir_dica == "1":
            tentativa = input("\nInsira a letra: ")
        elif jogar_ou_pedir_dica == "2":
            if dicas < 3:
                dicas = dicas + 1
                if dicas == 1:
                    print(dica1)
                elif dicas == 2:
                    print(dica2)
                else:
                    print(dica3)
            else:
                print("Suas dicas acabaram!")
            tentativa = input("\nInsira a letra: ")
        else: (print("\nOpção incorreta, insira a opção (1) ou (2): "))
        while tentativa in letras:
            print("Essa letra ja foi escolhida")
            tentativa = input("\nInsira a letra: ")
        letras.append(tentativa)

        if tentativa in palavraChave:
            print("Você acertou :)")
            for i in range(len(palavraChave)):
                if tentativa == palavraChave[i]:
                    palavra[i] = tentativa
        else:
            print("Você errou :(")
            tentativas = tentativas + 1
        print(palavra)
        print('as letras que você ja tentou são: ', letras)
        print("Você ja fez", tentativas, "tentativas erradas e ainda tem", chances - tentativas, "tentativas")

    if tentativas == chances:
        print("\nVocê perdeu :(")
        print("A palavra era:",palavraChave)
        perdeu = True
    else:
        print("Parabéns você ganhou :)")
        ganhou = True
    reiniciarJogo = input("\nJogar denovo? (1)Sim ; (2)Não: ")
    clean()
    if reiniciarJogo == "2":
        reiniciar = False
    else:
        reiniciar = True
    
    if perdeu:
        arquivo = open("historico.txt","a")
        arquivo.write("\nJogador: ")
        arquivo.write(nomeJogador)
        arquivo.write(", Desafiante: ")
        arquivo.write(nomeDesafiante)
        arquivo.write(", O vencedor foi: ")
        arquivo.write(nomeDesafiante)
        arquivo.write(", A palavra era: ")
        arquivo.write(palavraChave)

    elif ganhou:
        arquivo = open("historico.txt","a")
        arquivo.write("\nJogador: ")
        arquivo.write(nomeJogador)
        arquivo.write(", Desafiante: ")
        arquivo.write(nomeDesafiante)
        arquivo.write(", O vencedor foi: ")
        arquivo.write(nomeJogador)
        arquivo.write(", A palavra era: ")
        arquivo.write(palavraChave)