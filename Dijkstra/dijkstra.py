import math

def dijkstra(start: int, graph: dict):
    n = len(graph)

    # Inicjalizacja tablicy odległości
    distances = dict()
    for i in range(n):
        if i == start:
            distances[i] = {"dist" : 0,
                            "previous" : i}
        elif i in graph[start]:
            distances[i] = {"dist" : graph[start][i],
                            "previous" : start}
        else:
            distances[i] = {"dist" : math.inf,
                            "previous" : None}
            
    to_visit = set(graph.keys())
    to_visit.remove(start)

    while len(to_visit) > 0:
        min_dist = math.inf
        for w in to_visit:
            if distances[w]["dist"] < min_dist:
                v = w
                min_dist = distances[w]["dist"]
        
        to_visit.remove(v)

        for w in to_visit:
            if w in graph[v]:
                if distances[w]["dist"] > min_dist + graph[v][w]:
                    distances[w]["dist"] = min_dist + graph[v][w]
                    distances[w]["previous"] = v

    return distances


def route(museums: list, graph: dict):

    museums.sort()

    current_stop = 0
    time = 0
    route = [0]
    for i in museums:
        distances = dijkstra(start = current_stop, graph = graph)
        time += distances[i]["dist"]
        bus_stop = i
        subroute = []
        while True:
            if bus_stop == current_stop:
                break
            else:
                subroute.append(bus_stop)
                bus_stop = distances[bus_stop]["previous"]
        route = route + subroute[::-1]
        current_stop = i
    
    time += dijkstra(start = current_stop, graph = graph)[0]["dist"]
    route.append(0)

    return time, route
