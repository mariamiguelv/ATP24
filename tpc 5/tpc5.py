import random

sala1 = [50, [], "spider-man"]
sala2 = [70, [], "iron man"]
sala3 = [60, [], "avengers"]
sala4 = [80, [], "hulk"]

cinema = [sala1, sala2, sala3, sala4]

def mostrarMenu():
    print(''' Bem-vindo à nossa aplicação cinema!
              O que deseja fazer?
          
              -----------MENU--------------
              (1) Ver os filmes em exibição-------
              (2) Comprar bilhete----------
              (3) Disponibiliade de sala---
              (4) Inserir Sala-------------
              (0) Sair---------------------''')
  
    
def existeSala(cinema, sala): 
    cond = False
    for s in cinema:
      if s [2] == sala[2]:
        cond = True
      return cond
    
def inserirSala(cinema, sala):
    if not existeSala(cinema, sala):
      cinema.append(sala)
    return cinema
    
def listar(cinema): 
    if cinema:
      print("----Lista dos filmes em exibição!----")
      for s in cinema:
        print(f"Filme em exibição: {s[2]} | Lotação máxima da sala: {s[0]}")
    
    else:
       print("Nenhum filme em exibição no momento.")
    return
        
def disponivel(cinema, filmecinema, lugar): 
    cond = True
    for sala in cinema:
      nlugares, vendidos, filme = sala
      if filmecinema == filme and lugar <= nlugares:
        if lugar in vendidos:
           cond = False
    return cond
        
def venderBilhete(cinema, filmecinema, lugar):      
  for sala in cinema:
      nlugares, vendidos, filme = sala  
      if filme == filmecinema:
          if disponivel(cinema, filmecinema, lugar):
              vendidos.append(lugar)
              print(f"Lugar {lugar} comprado na sala do filme {filmecinema}.")
          else:
              print("O lugar {lugar} está indisponível para a sala do filme {filmecin}")
          return cinema
    
def listardisponibilidades(cinema):
    for sala in cinema:
        nlugares, vendidos, filme = sala
        disponiveis = nlugares - len(vendidos)
        print(f"O sala que exibe o filme {filme} tem {disponiveis} lugares disponíveis")

def cria_sala(cinema, filmecin, lugares):
    nova_sala = [int(lugares), [], filmecin]
    return inserirSala(cinema, nova_sala)
    
def sair():
    print("Saíste da aplicação. Até à próxima!")

def Menu():
  global cinema

  while True:
    mostrarMenu()
    opcao = int(input("Escolha uma opção!"))

    if opcao == 0:
      sair()
      break

    elif opcao == 1:
      listar(cinema)

    elif opcao == 2:
      filmecinema = input("Qual o fime que queres ver?")
      lugar = int(input("Número de lugar: ")) 
      cinema = venderBilhete(cinema, filmecinema, lugar)

    elif opcao == 3:
      listardisponibilidades(cinema)

    elif opcao == 4:
      filmecin = input("Qual filme deseja adicionar ao cinema?")
      lugares = input("Quantos lugares terá essa nova sala?")
      cinema = cria_sala(cinema, filmecin, lugares)

    else:
       print("Opção inválida. Tente novamente")
        
          
Menu()