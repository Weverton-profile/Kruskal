from networkx import Graph

def kruskal(grafo):
    resultado = []

    arestas = []

    # PEGANDO TODAS AS ARESTAS DO GRAFO
    for origem, conexoes in grafo.adjacency():
        for destino, peso in conexoes.items():
            arestas.append((origem, destino, peso['peso'])) 

    # ORDENA AS ARESTA COM BASE NO PESO
    arestas = sorted(arestas, key=lambda aresta: aresta[2])

    # BUSCAR OS CONJUNTOS
    subconjuntos = {v: v for v in grafo.nodes}

    for aresta in arestas:
        origem, destino, peso = aresta

        # VERIFICA SE NÃO ESTA EM UMA ORIGEM E DESTINO IGUAL
        if subconjuntos[origem] != subconjuntos[destino]:
            resultado.append(aresta)

            # UNIR OS CONJUNTOS
            novo_conjunto = subconjuntos[origem]
            antigo_conjunto = subconjuntos[destino]
            for v in subconjuntos:
                if subconjuntos[v] == antigo_conjunto:
                    subconjuntos[v] = novo_conjunto

    # CRIA O NOVO GRAFO COM A ARVORE GERADORA MINIMA
    novo_grafo = Graph()
    for origem, destino, peso in resultado:
        novo_grafo.add_edge(origem, destino, peso=peso)

    return novo_grafo

def criar_grafo():
    grafo = Graph()
    
    # OBS PARA O PROFESSOR: Nessa etapa do codigo eu coloquei duas formas de receber o grafo
    # Desse ponto ate o tracejado o codigo pode ser comentado caso queira usar um teste fixo
    # Esse ponto do codigo serve apenas para interação com o usuario
    vertices = int(input("Numero de vértices: "))
    arestas = int(input("Numero de arestas: "))

    for i in range(arestas):
        while True:
            try:
                partida, destino, peso = map(int, input(f"ORIGEM, DESTINO e PESO da aresta {i + 1}: ").split())
                if partida < 1 or partida > vertices or destino < 1 or destino > vertices or peso < 0:
                    print("ERRO: A ORIGEM e DESTINO devem estar entre 1 e", vertices, "o peso não pode ser um valor menor que 0")
                    continue
                break
            except ValueError:
                print("É aceito apenas numeros inteiros.")

        grafo.add_edge(partida, destino, peso=peso)
    # --------------------------------------------------------
    
    # Desse ponto em diante o codigo pode ser descomentado caso queira passar essa entrada padrão
    # Isso se o codigo de cima foi comentando, eliminando assim a interação
    # grafo.add_edge(1, 2, peso=7)
    # grafo.add_edge(1, 4, peso=5)
    # grafo.add_edge(2, 3, peso=8)
    # grafo.add_edge(2, 4, peso=9)
    # grafo.add_edge(2, 5, peso=7)
    # grafo.add_edge(3, 5, peso=5)
    # grafo.add_edge(4, 5, peso=15)
    # grafo.add_edge(4, 6, peso=6)
    # grafo.add_edge(5, 6, peso=8)
    # grafo.add_edge(5, 7, peso=9)
    # grafo.add_edge(6, 7, peso=11)

    return grafo

def print_grafo(grafo):
    for vertice, conexoes in grafo.adjacency():
        print(f"Vértice {vertice}:")
        for conexao, atributos in conexoes.items():
            peso = atributos['peso']
            print(f"  -> Conexão com vértice {conexao}, Peso: {peso}")

def carregar_grafo():
    grafo = criar_grafo()
    arvore_minima = kruskal(grafo)
    print_grafo(arvore_minima)

carregar_grafo()