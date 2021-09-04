from tree_intersection import __version__
from tree_intersection.hash_table import *
from tree_intersection.tree import *
from tree_intersection.tree_intersection import *

def test_version():
    assert __version__ == '0.1.0'



def test_tree_intersection():
    tree1=BinaryTree()
    root1=Node(100)
    root1.left=Node(200)
    root1.left.left=Node(300)
    root1.left.right=Node(400)
    root1.right=Node(500)
    root1.right.left=Node(600)
    tree1.root=root1

    tree2=BinaryTree()
    root=Node(100)
    root.left=Node(500)
    root.left.left=Node(1000)
    root.left.right=Node(600)
    root.right=Node(687)
    root.right.left=Node(7689)
    root.right.left.left=Node(300)

    tree2.root=root

    assert hash_map_tree_intersection(tree1,tree2)==[500,600,100,300]

