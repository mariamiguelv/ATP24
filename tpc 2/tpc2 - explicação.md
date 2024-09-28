O código que escrevi permite implementar um jogo de adivinhação, onde o jogador tem duas opções:
    Opção 1: o programa tenta adivinhar o número que o jogador pensou;
    Opção 2: o jogador tenta adivinhar o número que o programa pensou;

Caso o jogador escolha a opção 1, é importado um número aleatório através da função "random" que vai ser usado pelo computador para fazer palpites.
Defini variáveis: mínimo (0) e máximo (100) para conseguir deliniar a janela de valores que o computador iria usar para os seus palpites.
Assim aparece uma janela que pede ao jogador para pensar num número entre 0 e 100. É então gerado um palpite inicial através da expressão random.randrange(1,100). 
A seguir é pedido ao jogador para comentar no palpite dado, noemadamente, se o número é muito grande, muito pequeno ou o correto. 
Dependendo do feedback:
Se o número for muito pequeno, o código vai ajustar o mínimo para o palpite dado de modo a garantir que todos os próximos palpites seram maiores que o dado e o contador de palpites vai somar ao seu valor anterior ( de 0 passa para 1) e assim sucessivamente. 
É então gerado um novo palpite através da expressão random.randint(mínimo, máximo) com os novos valores.
Se o palpite for muito grande, então será o valor máximo será ajustado para que todos os próximos palpites sejam sempre menores que aquele. E ,seguindo a lógica do anterior, o contador aumenta 1 e é gerado um novo palpite.
Todo o processo continua até se acerrtar no número, em que o programa vai imprimir uma mensagem juntamente com o número de tentativas.

Caso o jogador escolha a opção 2, o computador vai gerar um número aleatório entre 1 e 100 (random,randrange(1,100)) sem o utilizador saber qual é esse número.
É então pedido ao jogador que faça uma série de palpites que terão como resposta se o palpite é muito baixo ou alto e, caso isso aconteça, então pede um novo palpite. O ciclo irá continuar até o jogador acertar no número gerado pelo computador. Cada vez que o jogador manda um palpite e não acerta é adicionador ao contador mais uma tentativa. No final quando o jogador adivinhar no número é devolvida a mensagem que acertou juntamente com o número de tentativas.