graph = { 
    'start': 
    { 
        'a': 6, 
        'b': 2 
    }, 
    'a': 
    { 
        'fin': 1
    }, 
    'b': 
    { 
        'a': 3, 
        'fin': 5 
    },
    'fin' : {}
}
costs = {'a': 6, 'b': 2, 'fin': float('inf') }
parents = { 'a': 'start', 'b': 'start', 'fin': None}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    print(lowest_cost_node, lowest_cost)
    return lowest_cost_node

node = find_lowest_cost_node(costs) # to get the key with the smaller value

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < cost:
            cost[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

    processed.append(graph.keys)
    














# graph['start'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2

