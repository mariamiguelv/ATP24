import json
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter


class TaskManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.carregar_data()


    def carregar_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            return []


    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)
        
    
    def criar_publicacao(self):
        new_publication = {
            "title": input("Título: "),
            "abstract": input("Resumo: "),
            "keywords": input("Palavras-chave (separadas por vírgula): "),
            "authors": [],
            "doi": input("DOI: "),
            "publish_date": input("Data de publicação (YYYY-MM-DD): "),
            "url": input("URL: ")
        }

        num_autors = int(input("Número de autores: "))
        for _ in range(num_autors):
            autor = {
                "name": input("Nome do autor: "),
                "affiliation": input("Afiliação: ")
            }
            new_publication["authors"].append(autor)

        self.data.append(new_publication)
        self.save_data()
        print("Publicação criada com sucesso!")


    def consultar_publicacao(self):
        while True:
            title = input("Insira o título ou parte dele: ").lower()
            results = [pub for pub in self.data if title in pub["title"].lower()]

            if results:
                for pub in results:
                    print("------------------------------------------------------------------------------------------")
                    print(f"Título: {pub['title']}\n \nResumo: {pub['abstract']}\n \nAutores: {[author['name'] for author in pub['authors']]}\n------------------------------------------------------------------------------------------\n")
                break
            else:
                print("Nenhuma publicação encontrada. Deseja tentar novamente?")
                if input().lower() != 'sim':
                    break


    def listar_publicacoes(self):
        for pub in self.data:
            print(f"Título: {pub['title']}\nData de publicação: {pub['publish_date']}\nAutores: {[author['name'] for author in pub['authors']]}\n")

    
    def listar_autores(self):
        autores = {}
        for pub in self.data:
            for autor in pub["authors"]:
                if autor["name"] not in autores:
                    autores[autor["name"]] = []
                autores[autor["name"]].append(pub["title"])

        for autor, artigos in sorted(autores.items()):
            print(f"Autor: {autor}\nPublicações: {', '.join(artigos)}\n")


    def delete_publicacao(self):
        while True:
            title = input("Insira o título da publicação a ser removida: ").lower()
            for i, pub in enumerate(self.data):
                if title in pub["title"].lower():
                    print(f"Removendo publicação: {pub['title']}")
                    del self.data[i]
                    self.save_data()
                    print("Publicação removida com sucesso.")
                    return
            print("Publicação não encontrada. Deseja tentar novamente?")
            if input().lower() != 'sim':
                break


    def gerar_relatorio(self):
        if not self.data:
            print("Nenhuma publicação disponível no sistema.")
            return

        print("\n--------Relatório de Estatísticas--------")
        # Frequência de palavras-chave
        keywords = [keyword for pub in self.data for keyword in pub["keywords"].split(",")]
        keywords_freq = Counter(keywords).most_common(20)
        print("\nPalavras-chave mais frequentes:")
        for keyword, freq in keywords_freq:
            keyword_limpo = keyword.replace(",", "")
            print(f"{keyword_limpo}: {freq} vezes")

        # Número de publicações por autor
        autores = [author["name"] for pub in self.data for author in pub["authors"]]
        autores_freq = Counter(autores).most_common(20)
        print("\nAutores com mais publicações:")
        for autor, freq in autores_freq:
            print(f"{autor}: {freq} publicações")

        # Número de publicações por ano
        anos = [datetime.strptime(pub["publish_date"], "%Y-%m-%d").year for pub in self.data]
        anos_freq = Counter(anos).most_common()
        print("\nNúmero de publicações por ano:")
        for ano, freq in anos_freq:
            print(f"{ano}: {freq} publicações")
        print("----------------------------------------")


# ------------------------------------------------------------------------------------------------------------------------------------------


class Menu:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def mostrar_ajuda(self):
        print("╔════════════════════════════════════════════════════════════╗")
        print("║                      Ajuda do Sistema                      ║")
        print("╠════════════════════════════════════════════════════════════╣")
        print("║  2 Criar Publicação:                                       ║")
        print("║     Permite criar uma nova publicação inserindo título,    ║")
        print("║     resumo, palavras-chave, autores, data de publicação,   ║")
        print("║     e URL.                                                 ║")
        print("║  3. Consultar Publicação:                                  ║")
        print("║     Pesquisa publicações por título (ou parte dele)        ║")
        print("║     e exibe os resultados detalhados.                      ║")
        print("║  4. Listar Publicações:                                    ║")
        print("║     Lista todas as publicações com os respetivos títulos   ║")
        print("║     e datas de publicação.                                 ║")
        print("║  5. Listar Autores:                                        ║")
        print("║     Exibe todos os autores no sistema, junto com as suas   ║")
        print("║     publicações.                                           ║")
        print("║  6. Apagar Publicação:                                     ║")
        print("║     Permite apagar uma aplicação através do seu título.    ║")
        print("║  7. Gerar Relatório:                                       ║")
        print("║     Gera um relatório com estatísticas sobre palavras-     ║")
        print("║     chave, autores e número de publicações por ano.        ║")
        print("║  8. Sair:                                                  ║")
        print("║     Salva os dados no ficheiro e encerra o programa.       ║")
        print("╚════════════════════════════════════════════════════════════╝")


    def exibir_menu(self):
        while True: 
            print("╔══════════════════════════════════╗")
            print("║         Menu Principal           ║")
            print("╠══════════════════════════════════╣")
            print("║  1. Help                         ║")
            print("║  2. Criar Publicação             ║")
            print("║  3. Consultar Publicação         ║")
            print("║  4. Listar Publicações           ║")
            print("║  5. Listar Autores               ║")
            print("║  6. Apagar Publicação            ║")
            print("║  7. Gerar Relatório              ║")
            print("║  8. Sair                         ║")
            print("╚══════════════════════════════════╝")

            option = input("Escolha uma opção: ")

            if option == "1":
                self.mostrar_ajuda()    
            elif option == "2":
                self.task_manager.criar_publicacao()
            elif option == "3":
                self.task_manager.consultar_publicacao()
            elif option == "4":
                self.task_manager.listar_publicacoes()
            elif option == "5":
                self.task_manager.listar_autores()
            elif option == "6":
                self.task_manager.delete_publicacao()
            elif option == "7":
                self.task_manager.gerar_relatorio()
            elif option == "8":
                self.task_manager.save_data()
                print("Dados salvos. A sair...")
                break
            else:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    task_manager = TaskManager("publicacoes.json")
    menu = Menu(task_manager)
    menu.exibir_menu()