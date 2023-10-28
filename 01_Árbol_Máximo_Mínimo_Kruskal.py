import networkx as nx

# Crear un grafo no dirigido con pesos en las aristas
G = nx.Graph()

# Agregar nodos
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')

# Agregar aristas con pesos
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=4)
G.add_edge('B', 'D', weight=5)

# Función para encontrar el árbol de expansión mínima (Kruskal)
def kruskal_min_spanning_tree(graph):
    mst = nx.minimum_spanning_tree(graph)
    return mst

# Función para encontrar el árbol de expansión máxima
def max_spanning_tree(graph):
    max_tree = nx.maximum_spanning_tree(graph)
    return max_tree

# Encontrar el árbol de expansión mínima
min_tree = kruskal_min_spanning_tree(G)
print("Árbol de expansión mínima (Kruskal):")
print(min_tree.edges(data=True))

# Encontrar el árbol de expansión máxima
max_tree = max_spanning_tree(G)
print("\nÁrbol de expansión máxima:")
print(max_tree.edges(data=True))
