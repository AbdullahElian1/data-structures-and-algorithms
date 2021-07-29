import pytest
from linked_list import __version__
from linked_list.linked import LinkedList, Node


def test_version():
    assert __version__ == '0.1.0'

def test_instance_node():
  assert Node()

def test_if_node_has_vlaue():
  node = Node("Test")
  actual = node.value
  assert actual == "Test"

def test_node_has_next_property():
  node = Node("test")
  actual = node.next
  assert True


def test_linkedlist():
   assert LinkedList()
def test_insert():
  ll = LinkedList()
  with pytest.raises(AttributeError):
    ll.head.value
  ll.insert(15)
  actual = ll.head.value
  assert actual == 15

def test_fined_value_in_linked_list():
    new_linked= LinkedList()
    new_linked.insert(5)
    assert new_linked.includes(5)

def test_fined_value_in_linked_list():
    new_linked= LinkedList()
    with pytest.raises(AttributeError):
        new_linked.head.value
    new_linked.insert(5)
    assert new_linked.includes(3)==False




