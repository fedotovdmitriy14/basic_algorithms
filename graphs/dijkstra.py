graph = {
    'start': {
        'A': 6,
        'B': 2
    },
    'A': {
        'finish': 1
    },
    'B': {
        'A': 3,
        'finish': 5
    },
    'finish': {}
}

costs = {
    'A': 6,
    'B': 2,
    'finish': float('inf')
}

parents = {
    'A': 'start',
    'B': 'start',
    'finish': None
}


processed = set()


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_algorithm(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        print(node)
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs)
    final_way = show_final_way(parents)
    return final_way


def show_final_way(parents):
    finish = parents['finish']
    final_way = ['finish']
    while True:
        if finish == 'start':
            final_way.append('start')
            break
        final_way.append(finish)
        finish = parents[finish]
    return final_way[::-1]


print(dijkstra_algorithm(graph, costs, parents))
