from tree_intersection.hash_table import  HashTable
from tree_intersection.linked_list import LinkedList
from tree_intersection.tree import *



def hash_map_tree_intersection(tree1,tree2):
    arr=[]
    arr1=tree2.in_order(tree2.root)
    hash=HashTable()
    print(tree1.root.value)
    def convert_tree_to_hash(root):

            if root.left:
                convert_tree_to_hash(root.left)

            hash.add(str(root.value),str(root.value))

            if root.right:
                convert_tree_to_hash(root.right)


    convert_tree_to_hash(tree1.root)

    for i in arr1:
        if hash.contains(str(i)):
            arr.append(i)
    return arr








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
# print(tree1.in_order(root1))
print(hash_map_tree_intersection(tree1,tree2))
