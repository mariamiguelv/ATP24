tabMeteo1 = [((2022,1 ,20), 2, 16, 0), ((2022,1,21),1,13,0.2), ((2022,1,22),7, 17, 0.01)]

def mostrarMenu():
    print('''--------------------------------MENU-------------------------------
             1)--Temperatura média diária---------------------------------------
             2)--Guardar tabela em ficheiro-------------------------------------
             3)--Carregar a tabela----------------------------------------------
             4)--Temperatura mínima mais baixa----------------------------------
             5)--Amplitude média térmica----------------------------------------
             6)-- Precipitação máxima-------------------------------------------
             7)--Dias com precepitação superiores a p---------------------------
             8)--Maior número consecutivo de dias com precipitaão abaixo de p---
             9)--Gráficos da temperatura máxima, mínima e pluvosidade-----------
             0)--Sair-----------------------------------------------------------''')
    

def Medias(tabMeteo):
    res = []
    for data, min, max,_ in tabMeteo:
        media  = (min + max) / 2
        res.append((data, media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for dia in t:
        data, min, max, prec = dia
        ano, mes, dia = data
        registo = f"{ano}-{mes}-{dia} | {min} | {max} | {prec} \n"
        file.write(registo)
    file.close()
    
def carregaTabMeteo(fnome):
        res = []
        file = open(fnome, "r")
        for linha in file:
            linha = linha.strip()
            campos = linha.split(" | ")
            data, min, max, prec = campos
            ano ,mes, dia = data.split("-")
            dia = (int(ano), int(mes), int(dia), float(min), float(max), float(prec))
            res.append(dia)
        file.close()
        return res

def minTMin(tabMeteo):
    minimo = tabMeteo[0][1]
    for data, min, *_ in tabMeteo:
         if minimo > min:
              minimo = min
    return minimo
              
def amplTerm(tabMeteo):
     res= []
     for dia in tabMeteo:
          data, min, max, _ = dia
          amplitude = max - min
          res.append((data, amplitude))
     return res

def maxPrec(tabMeteo):
    max_prec = tabMeteo1[0][3]
    lista = []
    for data, min, max, prec in tabMeteo:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)

def diasPrecSup(tabMeteo, p):
    res = []
    for dia in tabMeteo:
        if dia[3] > p:
            res.append((dia[0], dia[3]))
    return res

def maxSemChuva(tabMeteo, p):
    consecLocal = 0
    consecGlobal = 0
    for data, min, max, prec in tabMeteo:
        if prec < p:
            consecLocal += 1
        else:
            if consecLocal > consecGlobal:
                consecGlobal = consecLocal
            consecLocal = 0
    if consecLocal > consecGlobal:
        consecGlobal = consecLocal
    return consecGlobal

import matplotlib.pyplot as plt

def grafTabMeteo(t):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data,  *_ in t]
    temp_min = [ min for _, min, *_ in t] #y
    temp_max = [ max for _, _, max, _, in t]
    precs = [prec for _, _, _, prec in t]

    plt.plot(datas, temp_min, label = "temp. mínima")
    plt.plot(datas, temp_max, label = "temp. máxima")

    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.bar(datas, precs)
    plt.xlabel("Data")
    plt.ylabel("Precitação mm")
    plt.title("Precipitação")
    plt.show()
    return

def menu():
    while True:
        mostrarMenu()
        opcao = int(input("Selecione uma opção: "))
        
        if opcao == 0:
            print("Aplicação encerrada.")
            break
        elif opcao == 1:
            print(Medias(tabMeteo1))
        elif opcao == 2:
            guardaTabMeteo(tabMeteo1, "meteorologia.txt")
        elif opcao == 3:
            tabMeteo2 = carregaTabMeteo("meteorologia.txt") 
            print("Tabela carregada:", tabMeteo2)
        elif opcao == 4:
            print("Temperatura mínima mais baixa:", minTMin(tabMeteo1))
        elif opcao == 5:
            print("Amplitude térmica diária:", amplTerm(tabMeteo1))
        elif opcao == 6:
            print("Data e valor da precipitação máxima:", maxPrec(tabMeteo1))
        elif opcao == 7:
            p = float(input("Digite o valor de precipitação p: "))
            print("Dias com precipitação superior a p:", diasPrecSup(tabMeteo1, p))
        elif opcao == 8:
            p = float(input("Digite o valor de precipitação p: "))
            print("Maior sequência de dias com precipitação abaixo de p:", maxSemChuva(tabMeteo1, p))
        elif opcao == 9:
            grafTabMeteo(tabMeteo1)
        else:
            print("Opção inválida. Tente novamente.")

menu()