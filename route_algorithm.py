import numpy as np

class Vertice:    #definição do vértice ou nó do grafo
  #construtor que recebe parâmetro padrão e o rotulo que vai receber o nome da cidade
  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo    #atributo rotulo
    self.visitado = False   #visitado que inicialmente recebe valor falso
    self.distancia_objetivo = distancia_objetivo    #utilizado na Busca Gulosa como referencia
    self.adjacentes = []    #lista vazia para armazenar os adjacentes

  def adiciona_adjacente(self, adjacente):   #função que adiciona adjacente e recebe adjacente
    self.adjacentes.append(adjacente)        #atributo

  def mostra_adjacentes(self):               #função para mostrar a lista
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)

#classe necessária para representar a ligação
class Adjacente:
  def __init__(self, vertice, custo): #construtor receber vertice que liga uma cidade a outra e o custo que é a distância
    self.vertice = vertice
    self.custo = custo

class Grafo:                       #classe que vai juntar as duas classes (vértice e adjacente - Grafo completo
  arad = Vertice('Arad', 366)      #cadastro das cidades
  zerind = Vertice('Zerind', 374)
  oradea = Vertice('Oradea', 380)
  sibiu = Vertice('Sibiu', 253)
  timisoara = Vertice('Timisoara', 329)
  lugoj = Vertice('Lugoj', 244)
  mehadia = Vertice('Mehadia', 241)
  dobreta = Vertice('Dobreta', 242)
  craiova = Vertice('Craiova', 160)
  rimnicu = Vertice('Rimnicu', 193)
  fagaras = Vertice('Fagaras', 178)
  pitesti = Vertice('Pitesti', 98)
  bucharest = Vertice('Bucharest', 0)
  giurgiu = Vertice('Giurgiu', 77)

  #cadastrando os adjacentes de cada cidade (nó)
  arad.adiciona_adjacente(Adjacente(zerind, 75))   #cria-se um novo objeto com o vértice ao qual ele está ligado
  arad.adiciona_adjacente(Adjacente(sibiu, 140))
  arad.adiciona_adjacente(Adjacente(timisoara, 118))

  zerind.adiciona_adjacente(Adjacente(arad, 75))
  zerind.adiciona_adjacente(Adjacente(oradea, 71))

  oradea.adiciona_adjacente(Adjacente(zerind, 71))
  oradea.adiciona_adjacente(Adjacente(sibiu, 151))

  sibiu.adiciona_adjacente(Adjacente(oradea, 151))
  sibiu.adiciona_adjacente(Adjacente(arad, 140))
  sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
  sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

  timisoara.adiciona_adjacente(Adjacente(arad, 118))
  timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

  lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
  lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

  mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
  mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

  dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
  dobreta.adiciona_adjacente(Adjacente(craiova, 120))

  craiova.adiciona_adjacente(Adjacente(dobreta, 120))
  craiova.adiciona_adjacente(Adjacente(pitesti, 138))
  craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
  rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
  rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

  fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
  fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

  pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
  pitesti.adiciona_adjacente(Adjacente(craiova, 138))
  pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

  bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
  bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
  bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

grafo = Grafo()  #criação de um objeto com todas as ligações

class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = vertice
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

class Gulosa:             #Classe de busca
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False   #indica se o objetivo foi encontrado

  def buscar(self, atual):    #vai analisar o elemento que está sendo analisado no momento
    print('-------')
    print('Atual: {}'.format(atual.rotulo))   #atual: nome da cidade
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:                            #buscador será uma função recursiva que pára quando self.encontrado
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))   #número de adjacentes define o tamanho do vetor a ser criado
      for adjacente in atual.adjacentes:     #percorre cada adjacente
        if adjacente.vertice.visitado == False:    #adjacente é a classe que possui uma lista com vértice e visitado
          adjacente.vertice.visitado == True
          vetor_ordenado.insere(adjacente.vertice)  #adiciona as cidades adjacentes no vetor
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:   #se o vetor não estiver vazio executa-se nova busca
        self.buscar(vetor_ordenado.valores[0])

busca_gulosa = Gulosa(grafo.pitesti)   #Indicação do objetivo
busca_gulosa.buscar(grafo.sibiu)  