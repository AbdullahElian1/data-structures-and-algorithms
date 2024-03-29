import pytest
from tree import __version__
from tree.tree import *

def test_version():
    assert __version__ == '0.1.0'





@pytest.fixture
def data():

    root=Node("A")
    root.left=Node("B")
    root.left.left=Node("D")
    root.left.right=Node("E")
    root.right=Node("C")
    root.right.left=Node("F")
    return root

def test_get_max():

    x=Node(5)
    x.left=Node(68)
    x.right=Node(78)
    x.left.left=Node(8)
    x.right.right=Node(9)
    y=BinaryTree()
    y.root=x
    actual=y.tree_max()
    expected=78
    assert actual==expected

def test_breadthFirst(data):
    test=BinaryTree()
    actual=test.BreadthFirst(data)
    expected=['A', 'B', 'C', 'D', 'E', 'F']
    assert actual==expected

def test_empty_breadthfirst():
    root=""
    test=BinaryTree()
    with pytest.raises(Exception,match="Empty Tree"):
     actual=test.BreadthFirst(root)
     assert actual



def test_empty_binary_tree():
    assert BinaryTree()

def test_one_node_binary_tree():
    test=BinaryTree()
    node=Node(10)
    actual =test.pre_order(node)
    expected=[10]
    assert expected==actual

def test_one_node_left_right_binary_tree():
    test=BinaryTree()
    node=Node(10)
    node.left=Node(11)
    node.right=Node(12)
    expected_left=11
    actual_left =node.left.value
    expected_right=12
    actual1_right =node.right.value
    assert expected_left==actual_left
    assert expected_right==actual1_right

def test_pre_order(data):
    x=BinaryTree()

    actual=x.pre_order(data)
    expected=["A", "B", "D", "E", "C", "F"]
    assert actual==expected

def test_in_order(data):
    x=BinaryTree()

    actual=x.in_order(data)
    expected=["D", "B", "E", "A", "F", "C"]
    assert actual==expected

def test_post_order(data):
    x=BinaryTree()

    actual=x.post_order(data)
    expected=["D", "E", "B", "F", "C", "A"]
    assert actual==expected

def test_add_method():
    x = BinarySearch()
    x.add(7)
    x.add(8)
    x.add(6)
    x.add(5)
    x.add(150)
    x.add(19)
    x.add(111)
    x.add(115)
    x.add(10000)
    actual = x.in_order(x.root)
    expected = [5, 6, 7, 8, 19, 111, 115, 150, 10000]
    assert actual == expected


def test_Contains_method():
    x = BinarySearch()
    x.add(7)
    x.add(8)
    x.add(6)
    x.add(5)
    x.add(150)
    x.add(19)
    x.add(111)
    x.add(115)
    x.add(10000)

    assert x.Contains(4) == False
    assert x.Contains(5) == True
    assert x.Contains(6) == True
    assert x.Contains(3) == False

