O programa que criámos implementa o jogo dos 21 fósforos, seguindo as regras pedidas.
O programa começa por explicar as regras: 
    quem retirar o último fósforo perde.
O utilizador escolhe um dos dois modos:
    Modo 1: O jogador começa primeiro.
    Modo 2: O computador começa primeiro.
O utilizador introduz a sua escolha (1 ou 2). Caso escolha um número inválido, o programa termina com uma mensagem de erro.
O jogo decorre num ciclo while enquanto houver fósforos restantes.
Cada jogada alterna entre o jogador e o computador:
    Jogada do Jogador:
        O jogador é convidado a escolher entre 1 e 4 fósforos. O programa valida esta escolha para garantir que:
            É um número entre 1 e 4.
            Não ultrapassa o número de fósforos restantes.
        Caso contrário, a jogada é considerada inválida e o jogador deve repetir.
    Jogada do Computador:
        O computador realiza uma jogada simples: tira 1 ou 2 fósforos, dependendo do número restante.
Se o jogador ou o computador retirar o último fósforo, o jogo termina e declara-se o vencedor:
    Quem retira o último fósforo perde.
Pontos importantes do programa:
    A variável "fosforos" controla o número de fósforos restantes no jogo. Após cada jogada, é atualizado para refletir o número atual.
    O programa valida todas as jogadas do jogador:      
        Se o jogador tentar retirar um número inválido de fósforos (fora do intervalo 1-4 ou maior do que os fósforos restantes), o programa apresenta uma mensagem de erro e permite ao jogador tentar novamente.
    O programa alterna entre as jogadas do jogador e do computador utilizando uma variável booleana chamada jogador_primeiro. Esta variável é alternada após cada jogada.
    O computador faz jogadas simples e previsíveis, retirando 1 ou 2 fósforos, dependendo da situação.
    O programa exibe mensagens claras para o jogador, indicando o número de fósforos restantes, as jogadas feitas, e quem ganha ou perde o jogo.