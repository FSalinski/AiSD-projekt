'''
Główny skrypt projektu, w którym testujemy działanie zaimplementowanych
algorytmów
'''

from bin.generate_graphs import generate_spanning_tree, generate_graph
from Dijkstra.dijkstra import *
import random as rnd
rnd.seed(123)

def main():
    n = 20
    m = 37
    min_weight = 1
    max_weight = 10
    
    graph = generate_graph(n, m, min_weight, max_weight)

    print(graph)

    print(route([1, 3, 4, 8, 11, 16], graph))


if __name__ == '__main__':
    main()
