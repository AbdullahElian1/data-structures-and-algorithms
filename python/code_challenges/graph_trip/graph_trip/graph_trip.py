import sys

sys.path.append("/home/abdullah/Asac/data-structures-and-algorithms/python/code_challenges/graph")

from graph.graph import *


ver=Vertex('a')
ver2=Vertex('b')
# ver3=Vertex('d')
# ver4=Vertex('p')

graph=Graph()
graph.add_vertex(ver)

graph.add_vertex(ver2)
# graph.add_vertex(ver3)
# graph.add_vertex(ver4)

graph.add_edges(ver,ver2)
# graph.add_edges(ver,ver3)
# graph.add_edges(ver,ver4)

# print(len(graph.get_neighbors(ver)))

# print(graph.size()

# )
# print(graph._adjacency_list[f'{ver}'])



# graph._depthFirst(test)
# print(graph)

def business_trip(graph,arr):
    """
    Determine whether the trip is possible with direct flights, and how much it would cost.
    Args:
        graph (Graph): contains all the list of the cities and its cost
        arr (list): List of the cities
    Return
    """
    cost=0
    neighbors=graph.get_neighbors(arr[0])
    print(neighbors)
    # print(range(len(neighbors)))
    for city in neighbors:
        print("sss")
        if city.vertex.value == arr[1]:
            cost += city.weight
    # def one_city(city1,city2):
    return cost



print(business_trip(graph,["a","b"]))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree( self,p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        flag=False
        def walk(root1,root2):
            nonlocal flag
            if root1.val == root2.val:

                flag  = True

            else:
                return False
            walk(root1.left,root2.left)
            walk(root1.right,root2.right)

        walk(p,q)
        return flag


x= Solution

y=TreeNode(1)
y.left=TreeNode(2)

z=TreeNode(1)
z.left=TreeNode(2)
print(x.isSameTree(x,y,z))
