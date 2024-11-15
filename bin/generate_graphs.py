import random as rnd

def generate_graph(n, m, min_weight, max_weight):
    if m < n - 1 or m > n * (n - 1) / 2:
        raise ValueError("Invalid number of edges")
    if min_weight > max_weight:
        raise ValueError("Invalid weight range")
    
    graph = generate_spanning_tree(n, min_weight, max_weight)

    # Add the remaining edges
    for _ in range(m - (n-1)):
        u = rnd.randint(0, n-1)
        v = rnd.randint(0, n-1)
        while v == u or v in graph[u]:
            u = rnd.randint(0, n-1)
            v = rnd.randint(0, n-1)
        weight = rnd.randint(min_weight, max_weight)
        graph[u][v] = weight
        graph[v][u] = weight
    
    return graph

def generate_spanning_tree(n, min_weight, max_weight):
    tree = dict()
    for i in range(n):
        tree[i] = dict()

    # Choose random starting vertex
    u = rnd.randint(0, n-1)
    visited = set()
    visited.add(u)
    for _ in range(n-1):
        # Choose random edge
        while True:
            v = rnd.randint(0, n-1)
            if v in visited or v == u:
                u = v
                continue
            break
        # Choose random weight
        weight = rnd.randint(min_weight, max_weight)
        tree[u][v] = weight
        tree[v][u] = weight
        # Add the vertex to the visited set
        visited.add(v)
        
    return tree
