from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = None
        self._nodelist = []

    def get_year(self):
        return DAO.get_year()

    def get_shape(self, year):
        return DAO.get_shape(year)

    def crea_grafo(self, year, shape):
        self._grafo = nx.DiGraph()

        self._nodelist = DAO.get_nodes(year, shape)
        self._grafo.add_nodes_from(self._nodelist)

        for n1 in self._grafo.nodes:
            for n2 in self._grafo.nodes:
                if n1.id != n2.id and n1.state == n2.state:
                    if n1.datetime > n2.datetime:
                        self._grafo.add_edge(n1, n2)
                    elif n1.datetime < n2.datetime:
                        self._grafo.add_edge(n2, n1)

        n_connesse = nx.number_weakly_connected_components(self._grafo)
        max_connessa = max(nx.weakly_connected_components(self._grafo))

        print(f"Nodi: {len(self._grafo.nodes)}, Archi: {len(self._grafo.edges)}")
        print(f"Componenti connesse: {n_connesse}")
        max_connessa = max(nx.weakly_connected_components(self._grafo), key=len)
        print(f"Max connessa ha lunghezza {len(max_connessa)}")
        for n in max_connessa:
            print(n)
