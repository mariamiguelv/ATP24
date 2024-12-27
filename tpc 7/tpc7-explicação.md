Este programa foi desenvolvido para gerir dados meteorológicos e realizar várias operações, como cálculo de temperaturas médias, precipitação máxima e visualização gráfica das informações. O utilizador interage com o programa através de um menu que apresenta diferentes opções.
Relativamente à estrutura dos dados, Os dados meteorológicos são armazenados numa lista chamada tabMeteo1, onde cada elemento é um tuplo com os seguintes valores:
    Data: Um tuplo com o ano, mês e dia.
    Temperatura mínima (ºC).
    Temperatura máxima (ºC).
    Precipitação (em milímetros).
As principais funções são:
    mostrarMenu() - Apresenta o menu principal com as opções disponíveis para o utilizador.
    medias(tabMeteo) - calcula a temperatura média diária, somando a temperatura mínima e máxima de cada dia e dividindo por 2. O resultado é uma lista de tuplas com a data e a temperatura média.
    guardarTabMeteo(t, nome_ficheiro) - guarda os dados meteorológicos num ficheiro. Cada linha do ficheiro contém:
        A data no formato "ano-mês-dia".
        A temperatura mínima.
        A temperatura máxima.
        A precipitação.
    carregaTabMeteo(nome_ficheiro) - lê os dados meteorológicos de um ficheiro previamente guardado e reconstrói a lista com as informações.
    minTmin(tabMeteo) percorre os dados e retorna o valor mais baixo registado na coluna de temperaturas mínimas.
    amplTerm(tabMeteo) - calcula a amplitude térmica diária (diferença entre temperatura máxima e mínima) e retorna uma lista com as amplitudes.
    maxPrec(tabMeteo) - encontra o dia com o maior valor de precipitação e devolve a data e o valor registado.
    diasPrecSup(tabMeteo, p) - filtra os dias em que a precipitação foi superior a um valor fornecido pelo utilizador (p) e devolve uma lista com as datas e os valores.
    maxSemChuva(tabMeteo, p) - filtra os dias em que a precipitação foi superior a um valor fornecido pelo utilizador (p) e devolve uma lista com as datas e os valores.
    graficoTabMeteo(tabMeteo) - cria dois gráficos usando a biblioteca matplotlib:
        Gráfico de Linhas: Mostra a temperatura mínima e máxima ao longo dos dias.
        Gráfico de Barras: Mostra a precipitação diária.
A função menu() permite ao utilizador interagir com o programa. As opções do menu são:
    Temperatura média diária: Calcula e apresenta a temperatura média de cada dia.
    Guardar tabela em ficheiro: Guarda os dados meteorológicos num ficheiro chamado "meteorologia.txt".
    Carregar tabela de um ficheiro: Lê os dados de um ficheiro e apresenta-os.
    Temperatura mínima mais baixa: Mostra o valor mais baixo das temperaturas mínimas.
    Amplitude térmica média: Calcula a diferença entre temperatura máxima e mínima para cada dia.
    Precipitação máxima: Indica o dia e o valor da precipitação mais alta.
    Dias com precipitação superior a p: Mostra os dias em que a precipitação ultrapassou um valor fornecido.
    Maior sequência de dias sem chuva: Calcula o maior número consecutivo de dias com precipitação inferior a um valor.
    Gráficos: Gera gráficos da temperatura mínima, máxima e precipitação.
    Sair: Encerra a aplicação.


