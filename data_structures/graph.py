
class Graph:
    """
    Adjacency list representation of a graph.
    """
    def __init__(self):
        self.nodes = {}

    def __str__(self):
        string = ''
        for key, value in self.nodes.items():
            temp = key + ': ' + str(value)
            string = string + temp + '\n'

        return string

    def addnode(self,key):
        if key in self.nodes:
            print('Node already exists in the graph. Use a different key value.')
            return

        self.nodes[key] = []

    def addedge(self,key1,key2,value=1):
        if key1 in self.nodes and key2 in self.nodes:
            self.nodes[key1].append((key2,value))
        else:
            print('Source and terminal nodes must be valid nodes.')
            return


if __name__ == '__main__':
    graph = Graph()

    print(graph)
    graph.addnode('twelve')
    graph.addnode('forty-seven')
    graph.addedge('twelve','forty-seven',2)

    print(graph)