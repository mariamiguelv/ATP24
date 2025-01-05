import PySimpleGUI as sg
from linha_comando import TaskManager
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Inicializar o gerenciador de tarefas com o dataset
manager = TaskManager("publicacoes.json")


# Layout inicial do menu principal
def menu_layout():
    return [
        [sg.Text("Sistema de Consulta e Análise de Publicações Científicas", font=("Helvetica", 16), justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Button("Criar Publicação", key="-CRIAR-")],
        [sg.Button("Consultar Publicação", key="-CONSULTAR-")],
        [sg.Button("Atualizar Publicação", key="-ATUALIZAR-")],
        [sg.Button("Listar Publicações", key="-LISTAR_PUBLICACOES-")],
        [sg.Button("Listar Autores", key="-LISTAR_AUTORES-")],
        [sg.Button("Analisar Palavras-chave", key="-ANALISAR_PALAVRAS_CHAVE-")],
        [sg.Button("Gerar Relatório (Gráficos e Estatísticas)", key="-RELATORIO-")],
        [sg.Button("Sair", key="-SAIR-")]
    ]


# Função para layout de resultados
def resultado_layout(output):
    return [
        [sg.Text("Resultados", font=("Helvetica", 16), justification="center")],
        [sg.Multiline(output, size=(90, 30), disabled=True, key="-OUTPUT-")],
        [sg.Button("Voltar", key="-VOLTAR-")]
    ]


# Janela principal
sg.theme("LightGreen5")
window = sg.Window("Sistema de Publicações Científicas", menu_layout(), resizable=True, element_justification="center")


# Loop de eventos
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "-SAIR-"):
        manager.save_data()
        break

    elif event == "-CRIAR-":
        layout_criar = [
            [sg.Text("Título"), sg.Input(key="-TITULO-")],
            [sg.Text("Resumo"), sg.Multiline(key="-RESUMO-")],
            [sg.Text("Palavras-chave"), sg.Input(key="-KEYWORDS-")],
            [sg.Text("DOI"), sg.Input(key="-DOI-")],
            [sg.Text("Data de publicação (YYYY-MM-DD)"), sg.Input(key="-DATA-")],
            [sg.Text("URL"), sg.Input(key="-URL-")],
            [sg.Text("Número de Autores"), sg.Spin([i for i in range(1, 11)], initial_value=1, key="-NUM_AUTORES-")],
            [sg.Button("Adicionar", key="-ADD-"), sg.Button("Cancelar", key="-CANCELAR-")]
        ]
        window.close()
        window = sg.Window("Criar Publicação", layout_criar, resizable=True, modal=True)

        autores = []
        while True:
            event_criar, values_criar = window.read()

            if event_criar in (sg.WINDOW_CLOSED, "-CANCELAR-"):
                window.close()
                window = sg.Window("Sistema de Publicações Científicas", menu_layout(), resizable=True, element_justification="center")
                break

            elif event_criar == "-ADD-":
                for i in range(values_criar["-NUM_AUTORES-"]):
                    autor_nome = sg.popup_get_text(f"Nome do autor {i + 1}")
                    autor_afiliacao = sg.popup_get_text(f"Afiliação do autor {i + 1}")
                    autores.append({"name": autor_nome, "affiliation": autor_afiliacao})

                nova_publicacao = {
                    "title": values_criar["-TITULO-"],
                    "abstract": values_criar["-RESUMO-"],
                    "keywords": values_criar["-KEYWORDS-"],
                    "authors": autores,
                    "doi": values_criar["-DOI-"],
                    "publish_date": values_criar["-DATA-"],
                    "url": values_criar["-URL-"]
                }
                manager.data.append(nova_publicacao)
                manager.save_data()
                sg.popup("Publicação criada com sucesso!", title="Sucesso")
                window.close()
                window = sg.Window("Sistema de Publicações Científicas", menu_layout(), resizable=True, element_justification="center")
                break


    elif event == "-CONSULTAR-":
        titulo = sg.popup_get_text("Digite o título ou parte dele para buscar:", title="Consulta de Publicação")
        if titulo:
            results = [pub for pub in manager.data if titulo.lower() in pub["title"].lower()]
            if results:
                output = "\n\n".join([f"Título: {pub['title']}\nResumo: {pub['abstract']}\nAutores: {', '.join([author['name'] for author in pub['authors']])}\n" for pub in results])
            else:
                output = "Nenhuma publicação encontrada."

            window.close()
            window = sg.Window("Resultados da Consulta", resultado_layout(output), resizable=True, element_justification="center")


    elif event == "-LISTAR_PUBLICACOES-":
        output = "\n\n".join([f"Título: {pub['title']}\nData de publicação: {pub['publish_date']}\nAutores: {', '.join([author['name'] for author in pub['authors']])}" for pub in manager.data])
        window.close()
        window = sg.Window("Lista de Publicações", resultado_layout(output), resizable=True, element_justification="center")

        
    elif event == "-LISTAR_AUTORES-":
        autores = {}
        for pub in manager.data:
            for autor in pub["authors"]:
                if autor["name"] not in autores:
                    autores[autor["name"]] = []
                autores[autor["name"]].append(pub["title"])

        output = "\n\n".join([f"Autor: {autor}\nPublicações: {', '.join(artigos)}\n" for autor, artigos in sorted(autores.items())])
        window.close()
        window = sg.Window("Lista de Autores", resultado_layout(output), resizable=True, element_justification="center")


    elif event == "-ANALISAR_PALAVRAS_CHAVE-":
        # Contar a frequência de cada palavra-chave
        palavras_chave = {}
        for pub in manager.data:
            for palavra in pub["keywords"].split(","):
                palavra = palavra.strip().lower()
                if palavra:
                    if palavra not in palavras_chave:
                        palavras_chave[palavra] = []
                    palavras_chave[palavra].append(pub["title"])

        # Ordenar palavras-chave por frequência e alfabeticamente
        palavras_chave_ordenadas = sorted(palavras_chave.items(), key=lambda x: (-len(x[1]), x[0]))

        # Layout para exibir as palavras-chave
        layout_palavras = [
            [sg.Text("Palavras-chave e suas ocorrências:", font=("Helvetica", 16), justification="center")],
            [sg.Listbox(
                values=[f"{palavra} ({len(titulos)} ocorrências): {titulos}" for palavra, titulos in palavras_chave_ordenadas],
                size=(60, 20), key="-LISTA_PALAVRAS-", enable_events=True )],
            [sg.Button("Voltar", key="-VOLTAR-")]
        ]

        window.close()
        window = sg.Window("Análise de Palavras-chave", layout_palavras, resizable=True, modal=True)

        
    
    elif event == "-ATUALIZAR-":
        titulo = sg.popup_get_text("Digite o título da publicação para atualizar:", title="Atualizar Publicação")
        if titulo:
            publicacao = next((pub for pub in manager.data if pub["title"].lower() == titulo.lower()), None)
            if publicacao:
                layout_atualizar = [
                    [sg.Text("Título"), sg.Input(default_text=publicacao["title"], key="-TITULO-")],
                    [sg.Text("Resumo"), sg.Multiline(default_text=publicacao["abstract"], key="-RESUMO-")],
                    [sg.Text("Palavras-chave"), sg.Input(default_text=publicacao["keywords"], key="-KEYWORDS-")],
                    [sg.Text("Data de publicação (YYYY-MM-DD)"), sg.Input(default_text=publicacao["publish_date"], key="-DATA-")],
                    [sg.Text("DOI"), sg.Input(default_text=publicacao["doi"], key="-DOI-")],
                    [sg.Text("URL"), sg.Input(default_text=publicacao["url"], key="-URL-")],
                    [sg.Text("Número de Autores"), sg.Spin([i for i in range(1, 11)], initial_value=len(publicacao["authors"]), key="-NUM_AUTORES-")],
                    [sg.Button("Atualizar", key="-CONFIRMAR_ATUALIZAR-")],
                    [sg.Button("Cancelar", key="-CANCELAR-")]
                ]

                window.close()
                window = sg.Window("Atualizar Publicação", layout_atualizar, resizable=True, modal=True)

                while True:
                    event_atualizar, values_atualizar = window.read()

                    if event_atualizar in (sg.WINDOW_CLOSED, "-CANCELAR-"):
                        window.close()
                        window = sg.Window("Sistema de Publicações Científicas", menu_layout(), resizable=True, element_justification="center")
                        break

                    elif event_atualizar == "-CONFIRMAR_ATUALIZAR-":
                        publicacao.update({
                            "title": values_atualizar["-TITULO-"],
                            "abstract": values_atualizar["-RESUMO-"],
                            "keywords": values_atualizar["-KEYWORDS-"],
                            "publish_date": values_atualizar["-DATA-"],
                            "doi": values_atualizar["-DOI-"],
                            "url": values_atualizar["-URL-"]
                        })

                        # Atualizar autores
                        autores_atualizados = []
                        for i in range(values_atualizar["-NUM_AUTORES-"]):
                            autor_nome = sg.popup_get_text(f"Nome do autor {i + 1} (atual: {publicacao['authors'][i]['name'] if i < len(publicacao['authors']) else ''})")
                            autor_afiliacao = sg.popup_get_text(f"Afiliação do autor {i + 1} (atual: {publicacao['authors'][i]['affiliation'] if i < len(publicacao['authors']) else ''})")
                            autores_atualizados.append({"name": autor_nome, "affiliation": autor_afiliacao})

                        publicacao["authors"] = autores_atualizados
                        manager.save_data()
                        sg.popup("Publicação atualizada com sucesso!", title="Sucesso")
                        window.close()
                        window = sg.Window("Sistema de Publicações Científicas", menu_layout(), resizable=True, element_justification="center")
                        break        
        

    elif event == "-RELATORIO-":
        if not manager.data:
            sg.popup("Nenhuma publicação disponível no sistema.", title="Erro")
        else:
            # Frequência de palavras-chave
            keywords = [keyword.strip() for pub in manager.data for keyword in pub["keywords"].split(",")]
            keywords_freq = Counter(keywords).most_common(20)
            palavras, freq_palavras = zip(*keywords_freq)

            # Gráfico: Distribuição de palavras-chave mais frequentes
            plt.figure(figsize=(17, 6)) 
            plt.barh(palavras, freq_palavras, color='lightgreen')
            plt.xlabel('Frequência')
            plt.ylabel('Palavras-chave')
            plt.title('Top 20 Palavras-chave')
            plt.gca().invert_yaxis()
            plt.xticks(range(max(freq_palavras) + 1))
            plt.show()

            # Número de publicações por autor
            autores = [author["name"] for pub in manager.data for author in pub["authors"]]
            autores_freq = Counter(autores).most_common(20)
            autores, freq_autores = zip(*autores_freq)

            # Gráfico: Número de publicações por autor
            plt.figure(figsize=(17, 6))  
            plt.barh(autores, freq_autores, color='salmon')
            plt.xlabel('Número de Publicações')
            plt.ylabel('Autores')
            plt.title('Top 20 Autores com Mais Publicações')
            plt.gca().invert_yaxis()
            plt.xticks(range(max(freq_autores) + 1))
            plt.show()

            # Número de publicações por ano
            anos = [datetime.strptime(pub["publish_date"], "%Y-%m-%d").year for pub in manager.data]
            anos_freq = Counter(anos).most_common()
            anos, freq_anos = zip(*sorted(anos_freq))

            # Gráfico: Distribuição de publicações por ano
            plt.figure(figsize=(12, 6))  
            plt.bar(anos, freq_anos, color='skyblue')
            plt.xlabel('Ano')
            plt.ylabel('Número de Publicações')
            plt.title('Distribuição de Publicações por Ano')
            plt.xticks(range(min(anos), max(anos) + 1))
            plt.show()

            # Publicações por mês do ano 2024
            meses = [datetime.strptime(pub["publish_date"], "%Y-%m-%d").month for pub in manager.data if datetime.strptime(pub["publish_date"], "%Y-%m-%d").year == 2024]
            meses_freq = Counter(meses).most_common()
            meses, freq_meses = zip(*sorted(meses_freq))

            plt.figure(figsize=(12, 6))  
            plt.bar(meses, freq_meses, color='orange')
            plt.xlabel('Mês')
            plt.ylabel('Número de Publicações')
            plt.title('Distribuição de Publicações por Mês (2024)')
            plt.xticks(ticks=range(1, 13), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
            plt.yticks(range(max(freq_meses) + 1))
            plt.show()

            # Palavras-chave mais frequentes de 2024
            keywords_2024 = [keyword.strip() for pub in manager.data if datetime.strptime(pub["publish_date"], "%Y-%m-%d").year == 2024 for keyword in pub["keywords"].split(",")]
            keywords_2024_freq = Counter(keywords_2024).most_common(20)
            palavras_2024, freq_palavras_2024 = zip(*keywords_2024_freq)

            plt.figure(figsize=(12, 6))  
            plt.barh(palavras_2024, freq_palavras_2024, color='purple')
            plt.xlabel('Frequência')
            plt.ylabel('Palavras-chave')
            plt.title('Top 20 Palavras-chave de 2024')
            plt.gca().invert_yaxis()
            plt.xticks(range(max(freq_palavras_2024) + 1))
            plt.show()


    elif event == "-VOLTAR-":
        window.close()
        window = sg.Window("Sistema de Publicações Científicas", menu_layout(), resizable=True, element_justification="center")

window.close()