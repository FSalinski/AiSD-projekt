'''
Aplikacja umożliwiająca wpisywanie własnego grafu i szukania
w nim najtańszej ścieżki
'''

from Dijkstra.dijkstra import route


def main():
    while True:
        print("Zwiedzanie muzeów. Wybierz jedną z opcji:")
        print("1. Wpisz własny graf")
        print("2. Wylosuj graf")
        print("3. Sprawdź przykładowy graf")
        print("4. Zakończ program")
        option = int(input("Wybierz opcję: "))

        if option not in [1, 2, 3, 4]:
            print("Niepoprawna opcja")
            continue

        elif option == 1:
            while True:
                n = int(input("Podaj liczbę wierzchołków: "))
                m = int(input("Podaj liczbę krawędzi: "))

                if m < n - 1:
                    print("Za mało krawędzi")
                    continue
                if m > n * (n - 1) / 2:
                    print("Za dużo krawędzi")
                    continue
                
                graph = {}
                i = 0
                print("Wierzchołki są numerowane od 1 do", n)
                while i < m:
                    start = int(input(f"Podaj początek krawędzi {i + 1}: "))
                    end = int(input(f"Podaj koniec krawędzi {i + 1}: "))
                    weight = int(input(f"Podaj wagę krawędzi {i + 1}: "))

                    if start == end:
                        print("Początek i koniec krawędzi nie mogą być takie same")
                        continue

                    if start < 1 or start > n or end < 1 or end > n:
                        print("Niepoprawny wierzchołek")
                        continue

                    if weight <= 0:
                        print("Waga musi być większa od 0")
                        continue

                    if start not in graph:
                        graph[start] = {}
                    if end not in graph:
                        graph[end] = {}
                    if end not in graph[start]:
                        graph[start][end] = weight
                        graph[end][start] = weight
                        i += 1
                    else:
                        print("Krawędź już istnieje")
                        continue
                break
            i = 0
            museums = []
            while i < n:
                print("Czy wierzchołek", i + 1, "jest muzeum? (1/0)")
                is_museum = int(input())
                if is_museum == 1:
                    museums.append(i + 1)
                if is_museum not in [0, 1]:
                    print("Niepoprawna odpowiedź")
                    continue
                i += 1
            print("Wybrany graf:")
            print(graph)

            best_route = route(museums, graph)
            print("Najlepsza trasa:")
            print("Czas przejazdu:", best_route[0])
            print("Trasa:", ' -> '.join([str(x) for x in best_route[1]]))

        elif option == 2:
            pass

        elif option == 3:
            pass

        elif option == 4:
            pass


if __name__ == '__main__':
    main()