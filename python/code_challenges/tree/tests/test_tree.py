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


