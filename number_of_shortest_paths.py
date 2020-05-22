from collections import deque


def number_of_shortest_paths(graph, source):
    status = {node: 'undiscovered' for node in graph.nodes}
    distance = {node: float('inf') for node in graph.nodes}
    predecessor = {node: None for node in graph.nodes}
    shortest_paths = {node: float('inf') for node in graph.nodes}

    status[source] = 'pending'
    distance[source] = 0
    pending = deque([source])

    while pending:
        u = pending.popleft()
        for v in graph.neighbors(u):
            if status[v] == 'undiscovered':
                status[v] = 'pending'
                distance[v] = distance[u] + 1
                predecessor[v] = u
                pending.append(v)
                shortest_paths[v] = 1
            if status[v] == 'pending':
                shortest_paths[v] += 1
        status[u] = 'visited'

    return shortest_paths
