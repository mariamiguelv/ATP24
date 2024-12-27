O código que escrevi permite implementar uma aplicação de gestão de cinema, onde o utilizador é apresentado com várias opções para interagir com o programa.
Quando o programa é iniciado, é apresentado um menu com várias opções para o utilizador escolher. As funcionalidades implementadas incluem: ver os filmes em exibição, comprar bilhetes para os filmes disponíveis, verificar a disponibilidade de lugares nas salas, adicionar novas salas de cinema e por fim existe também a opção de sair do programa.
Caso o utilizador escolha a opção 1, aparece uma lista com todos os filmes que estão atualmente em exibição, juntamente com a capacidade máxima de cada sala. Se não houver filmes em exibição, é apresentada uma mensagem a informar que não há salas disponíveis.
Na opção 2, o utilizador pode comprar bilhetes para um determinafo filme. Primeiro, é pedido que o utilizador insira o nome do filme e o número do lugar pretendido. O programa vai então verificar, através da função "disponivel", se o lugar está disponível na sala correspondente ao filme. Caso o lugar esteja livre, ele é adicionado à lista de lugares vendidos, e é aparece a mensagem de confirmação da compra. Se o lugar já estiver ocupado, o programa informa que o lugar não está disponível.
A opção 3, permite verificar a disponibilidade de lugares em todas as salas. O programa percorre todas as salas e calcula o número de lugares ainda disponíveis em cada uma. Para cada sala, é apresentada a informação do filme em exibição e a quantidade de lugares livres.
Se o utilizador escolher a opção 4, pode adicionar uma nova sala ao cinema. Para isso, é pedido o nome do filme e o número total de lugares que a sala terá. O programa verifica se o filme já está em exibição, para evitar duplicações, e adiciona a nova sala ao cinema caso esta ainda não exista.
Por fim, a opção 0 encerra o programa. É apresentada uma mensagem de despedida, e o utilizador sai da aplicação.
Relativamente ao seu funcionamento, o programa vai utilizar as seguintes funções:
"listar": Apresenta a lista de filmes em exibição, juntamente com a capacidade máxima de cada sala.
"disponivel": Verifica se um determinado lugar está disponível numa sala específica.
"venderBilhete": Regista a compra dos bilhetes, adicionando o lugar à lista de lugares vendidos na sala correspondente.
"listardisponibilidades": Calcula e mostra a quantidade de lugares ainda disponíveis em cada sala.
"cria_sala": Cria uma nova sala com o filme especificado e adiciona-a ao cinema, se ainda não existir.
"existeSala": Verifica se uma sala já existe no cinema, através do nome do filme.
"inserirSala": Adiciona uma nova sala ao cinema, se não provocar duplicações.
Em suma, o programa apresenta um menu ao utilizador com diferentes opções.
O utilizador escolhe uma opção e insere os dados necessários (por exemplo,o nome do filme ou o número do lugar).
O programa executa a funcionalidade correspondente e apresenta o resultado ao utilizador.
O ciclo continua até o utilizador escolher a opção "0", que encerra o programa.
