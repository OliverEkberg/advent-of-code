import networkx as nx

lines = [line.strip() for line in open(0)]

G = nx.Graph()

for line in lines:
    n1, n2 = line.split('-')
    G.add_edge(n1, n2)

print(sum(
    any(node.startswith('t') for node in clique)
    for clique in nx.enumerate_all_cliques(G)
    if len(clique) == 3
))

print(','.join(sorted(max(nx.find_cliques(G), key=len))))
