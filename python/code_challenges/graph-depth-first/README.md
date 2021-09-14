# graph-depth-first
Challenge
    to return the Deepth path in graph


# Efficiency for breadth first

    Time: O(n)
    Space: O(n)

# Solution
'''
def _depthFirst(self, action=lambda x: print(x)):
    """
    Performs a depth first travesal of the graph and calls action at each node
    """
    depthFirst=Stack()
    visited=[]


    vertex=list(self._adjacency_list.keys())[0]
    vertex=Vertex(vertex)
    depthFirst.push(vertex)

    visited.append(vertex.value)


    while not depthFirst.is_empty():
        top=depthFirst.peek()

        action(top.value)

         # call action here
        list_edges=self._adjacency_list[f"{top}"]

        for edge in list_edges:
            if not (edge.vertex.value in  visited):
                # print(edge.vertex)
                visited.append(edge.vertex.value)
                depthFirst.push(edge.vertex)
        depthFirst.pop()

    return visited

'''
