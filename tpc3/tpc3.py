
print("Bem-vindo ao Jogo dos 21 Fósforos!")
print("Regras: Quem tirar o último fósforo perde.")
print("Escolha o modo:")
print("1 - Jogador começa primeiro")
print("2 - Computador começa primeiro")


modo = int(input("Escolha (1 ou 2): "))
fosforos = 21

if modo == 1:
    jogador_primeiro = True
elif modo == 2:
    jogador_primeiro = False
else:
    print("Escolha inválida. O jogo será encerrado.")
    exit()

while fosforos > 0:
    print(f"\nFósforos restantes: {fosforos}")
    
    if jogador_primeiro:
        jogada = int(input("Quantos fósforos queres tirar (1-4)? "))
        if jogada < 1 or jogada > 4 or jogada > fosforos:
            print("Jogada inválida. Escolhe um número entre 1 e 4, sem ultrapassar os fósforos restantes.")
            continue
        fosforos -= jogada
        if fosforos == 0:
            print("Tiraste o último fósforo. Perdes-te!")
            break

    else:
        jogada_computador = 1 if fosforos <= 4 else 2  # Computador joga sem estratégias complexas
        print(f"O computador tirou {jogada_computador} fósforos.")
        fosforos -= jogada_computador
        if fosforos == 0:
            print("O computador tirou o último fósforo. Ganhaste!")
            break

    jogador_primeiro = not jogador_primeiro
