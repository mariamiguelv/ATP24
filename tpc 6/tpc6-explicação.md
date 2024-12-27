Através deste programa conseguimos gerir uma escola com várias turmas e alunos. A nossa estrutura principal é a escola, onde cada elementos irá representar uma turma. Cada turma terá um nome e uma lista de alunos, cada aluno, terá um nome, um ID e lista com 3 notas: notas do TPC, Projeto e teste.
Inicialmente temos um menu interativo que vai apresentar as seguintes opões que o utlizador poderá escolher:
opção 1 - criar uma nova turma - criar um nova turma e adicioná-la à lista de turmas na escola
opção 2 - inserir um aluno na turma - permite adicionar um aluno a uma turma específica. Tem de se inserir o nome, ID e as 3 notas do aluno.
opção 3 - listar alunos de um turma - lista os alunos de uma determinada turma dando como resposta o seu nome, ID e as notas.
opção 4 - consultar um aluno por ID - conseguimos procurar um aluno específico usando o seu ID e o nome da turma.
opção 5 - guardar uma turma num ficheiro - conseguimos guardar os dados de uma turma num ficheiro de texto. Cada linha de texto vai representar um aluno com o seu nome, ID e as suas notas.
opção 6 - carregar uma turma de um ficheiro - permite recuperarr os dados previamente guardados de uma turma num ficheiro de texto.
opção 7 - sair da aplicação - encerra o programa.
Relativamente às funcionalidades do sistema:
  existeTurma(nome_turma, escola) - verifica se uma turma com o nome dado já existe na lista de turmas da escola.
  criarTurma(nome_turma,escola) - verifica se a turma com o nome indicado (nome_turma) já existe. Caso contrário, adiciona uma nova turma (inicialmente vazia) à escola.
  inserirAluno(nome_turma,aluno) - verifica se a turma existe e, caso exista, adiciona o aluno à lista de alunos dessa turma. Se um aluno com o mesmo ID já existir na turma, a operação é rejeitada.
  listarTurma(nome_turma) - apresenta uma lista de todos os alunos de uma turma específica, com o respetivo nome, ID e notas.
  consultarAluno(id_aluno, nome_turma) - permite procurar um aluno específico pelo seu ID numa turma. Se o aluno existir, as suas informações são apresentadas.
  guardarTurma(nome_turma, fnome) - guarda todos os alunos de uma turma num ficheiro de texto. Cada linha contém as informações de um aluno (nome, ID e notas).
  recuperarTurma(fnome) - lê os dados de um ficheiro de texto e cria uma lista de alunos com base nas informações armazenadas. Estes dados podem ser posteriormente associados a uma nova turma.
  MostrarMenu() apresenta o menu principal e explica as opções disponíveis.
A função Menu é responsável por gerir o fluxo principal da aplicação. Ela apresenta o menu de opções ao utilizador, recebe a escolha e executa as funcionalidades correspondentes com base na opção selecionada. Caso seja inserida uma opção inválida, por exemplo, um número que não corresponda a nenhuma opção, então o programa vai apresentar a mensagem "Opção inválida. Tente novamente."
Um ponto importante também a referir é que nas funções existeTurma, criarTurma, inserirAluno, listarTurma, consultarTurma, guardarTurma é usada a conversão para letras minúsculas para eliminar problemas relacionados com letras maiúsculas e miniscúlas, e assim conseguimos garantir uma maior flexibilidade de ultização.