turma1 = [
    ("João Marinho", "A1010", [19, 17, 13]),
    ("Maria Soares", "A2020", [17, 15, 11]),
    ("Pedro Monteiro", "A3030", [15, 13, 8]),
    ("Carlos silva", "A3030", [20, 19, 16])
]

turma2 =[
    ("Mariana Ferreira","A4040",[13,16,11]),
    ("Joana Caravlho", "A5050", [14,19,13]),
    ("Inês Dias", "A6060", [15,17,12])
]

escola = [("turma1", turma1), ("turma2", turma2)]

def MostrarMenu():
    print('''Bem vindo à aplicação de gestão de alunos.
            1)----Criar uma turma---------------------------
            2)----Inserir um aluno na turma-----------------
            3)----Listar uma turma----------------------------
            4)----Consultar um aluno por id-----------------
            5)----Guardar a turma em ficheiro---------------
            6)----Carregar uma turma dum ficheiro-----------
            0)----Sair da aplicação-------------------------''' )

def existeTurma(nome_turma, escola):
    nome_turma = nome_turma.lower()  
    return any(turma_nome.lower() == nome_turma for turma_nome, _ in escola)

def criarTurma(nome_turma, escola):
    nome_turma = nome_turma.lower()
    if not existeTurma(nome_turma, escola):
        escola.append((nome_turma, []))
        print(f"A turma {nome_turma} foi criada!")
    else:
        print("Essa turma já existe!")

def inserirAluno(nome_turma, aluno):
    nome_turma = nome_turma.lower()
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            if aluno[1] not in [a[1] for a in turma_alunos]:
                turma_alunos.append(aluno)
                print(f"O {aluno[0]} foi adicionado na turma {nome_turma}.")
            else:
                print("Já existe na turma um aluno com o mesmo ID .")
            return
    print("Turma não existe.")

def listarTurma(nome_turma):
    nome_turma = nome_turma.lower()
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            print(f"--- Lista de alunos na turma {nome_turma} ---")
            for aluno in turma_alunos:
                print(f"Aluno: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
            return
    print("Turma não existe.")

def consultarAluno(id_aluno, nome_turma):
    nome_turma = nome_turma.lower()
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            for aluno in turma_alunos:
                if aluno[1] == id_aluno:
                    print(f"Aluno encontrado: Nome: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
                    return
    print("Aluno não existe.")

def guardarTurma(nome_turma, fnome):
    nome_turma = nome_turma.lower()
    file = open(fnome, "w")
    for turma_nome, turma_alunos in escola:
        if turma_nome.lower() == nome_turma:
            for aluno in turma_alunos:
                nome, id, [notaTPC, notaProj, notaTeste] = aluno
                file.write(f"{nome}, {id} |{notaTPC}|{notaProj}|{notaTeste}|")
                file.write("\n")

            print(f"Turma '{nome_turma}' foi guardada com sucesso em '{fnome}'.")
            file.close()
            return
        print("Turma não existe.")
    

def recuperarTurma(fnome):
    turma = []
    with open(fnome, "r") as file:  
        for line in file:
            partes = line.strip().split("|")  
            if len(partes) >= 2: 
                nome, id = partes[0].split(",")  
                notas = list(map(int, partes[1].split("|")))  
                aluno = (nome, id, notas) 
                turma.append(aluno)  
    if turma: 
        print("Turma recuperada do ficheiro:")
        for aluno in turma:
            print(f"Aluno: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
    else:
        print("Nenhuma turma foi recuperada ou o arquivo está vazio.")


def Menu():
    global escola
    
    while True:
        MostrarMenu()
        opcao = int(input("O que queres fazer?"))
        
        if opcao == 0:
            print("Saíste da aplicação! Até à próxima!")
            break

        elif opcao == 1:
            nome_turma = input("Qual é o nome da turma que deseja criar? ").lower()
            criarTurma(nome_turma, escola)

        elif opcao == 2:
            nome_turma = input("Em que turma quer adicionar o aluno? ").lower()
            id_aluno = input("Inserir id do aluno: ")
            nome = input("Inserir nome: ")
            notaTPC = int(input("Nota do TPC? "))
            notaProj = int(input("Nota do projeto? "))
            notaTeste = int(input("Nota do teste? "))
            aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
            inserirAluno(nome_turma, aluno)

        elif opcao == 3:
            nome_turma = input("Qual é o nome da turma que deseja listar? ").lower()
            listarTurma(nome_turma)

        elif opcao == 4:
            nome_turma = input("Nome da turma do aluno: ").lower()
            id_aluno = input("qual é o Id do aluno a procurar? ")
            consultarAluno(id_aluno, nome_turma)

        elif opcao == 5:
            nome_turma = input("Qual é o nome da turma a guardar? ").lower()
            guardarTurma(nome_turma, "turma.txt")

        elif opcao == 6:
            turma = recuperarTurma("turma.txt")
            nome_turma = input("Qual é a turma que quer recuperar? ").lower()
            escola.append((nome_turma, turma))
        else:
            print("Opção inválida. Tente novamente.")

Menu()
