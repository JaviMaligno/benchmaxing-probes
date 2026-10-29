# Max closed trail (no repeated edge) in an m x n grid graph of cells.
# = max number of edges in a connected even-degree subgraph
# = |E| - (min T-join, T = odd-degree vertices), provided the remainder is connected.
# Min T-join computed exactly via min-weight perfect matching on shortest-path distances,
# then the complement is checked to be connected with all degrees even (so an Euler circuit exists).
import itertools, networkx as nx

def solve(m, n, check_conn=True):
    G = nx.grid_2d_graph(m, n)
    E = G.number_of_edges()
    T = [v for v in G if G.degree(v) % 2]
    dist = dict(nx.all_pairs_shortest_path_length(G))
    K = nx.Graph()
    for a, b in itertools.combinations(T, 2):
        K.add_edge(a, b, weight=-dist[a][b])
    M = nx.max_weight_matching(K, maxcardinality=True)
    # realize the T-join as symmetric difference of shortest paths
    J = set()
    for a, b in M:
        p = nx.shortest_path(G, a, b)
        for e in zip(p, p[1:]):
            e = frozenset(e)
            J ^= {e}
    tj = sum(dist[a][b] for a, b in M)
    H = G.copy()
    H.remove_edges_from([tuple(e) for e in J])
    H.remove_nodes_from([v for v in list(H) if H.degree(v) == 0])
    assert all(d % 2 == 0 for _, d in H.degree())
    assert H.number_of_edges() == E - tj  # J is a minimum T-join
    # E - tj is an upper bound; it is attained iff this optimal remainder is connected
    if not check_conn:
        return E - tj
    assert nx.is_connected(H) and nx.is_eulerian(H)
    return H.number_of_edges()

# brute-force cross-check on tiny grids: max even connected subgraph by enumeration
def brute(m, n):
    G = nx.grid_2d_graph(m, n); edges = list(G.edges()); best = 0
    for mask in range(1 << len(edges)):
        S = [edges[i] for i in range(len(edges)) if mask >> i & 1]
        if len(S) <= best: continue
        H = nx.Graph(S)
        if all(d % 2 == 0 for _, d in H.degree()) and nx.is_connected(H):
            best = len(S)
    return best
for (a, b) in [(2, 3), (3, 3), (3, 4), (2, 6)]:
    ub, bf = solve(a, b, check_conn=False), brute(a, b)
    assert bf <= ub, (a, b)
    print(f"  {a}x{b}: upper bound {ub}, brute force {bf}")
print("brute-force cross-check on small grids: OK")

orig = solve(11, 11)
print("original 11x11:", orig)
assert orig == 200
print("variant 9x13:", solve(9, 13))
