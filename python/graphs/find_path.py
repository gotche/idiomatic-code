'''
Implement a solution to find the ratios between currencies, given a list of them

'''
def find_ratio(graph, weights, source, destination, visited=None):
    if source == destination:
        return 1

    visited = visited or set()
    for node in graph[source]:
        if node not in visited:
            visited.add(node)
            subratio = find_ratio(graph, weights, node, destination, visited)
            if subratio is not None:
                subratio *= weights[(source, node)]
                return subratio


class Weight(dict):
    def __missing__(self, key):
        return 1/self[key[1], key[0]]


g = {'eur': ('usd', 'gbp'), 'usd': ('eur', ), 'gbp': ('eur', )}
w = Weight({('eur', 'usd'): 0.8, ('eur', 'gbp'): 1.1})


print(find_ratio(g, w, 'eur', 'gbp'))
