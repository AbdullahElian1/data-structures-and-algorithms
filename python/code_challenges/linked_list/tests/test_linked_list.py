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

def test_add_to_last_list():
    new_linked= LinkedList()
    new_linked.append(30)
    new_linked.append(35)
    actual=new_linked.head.next.value
    expect=35
    assert actual==expect

def test_add_many_to_last_list():
    new_linked= LinkedList()
    new_linked.append(30)
    new_linked.append(35)
    new_linked.append(40)
    new_linked.append(45)
    actual=new_linked.head.next.next.next.value
    expect=45
    assert actual==expect

def test_add_to_middle():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_before(20,30)
    actual=new_linked.head.next.value
    expect=30
    assert actual==expect

def test_add_befor_the_first():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_before(111,30)
    actual=new_linked.head.value
    expect=30
    assert actual==expect

def test_add_after_middle():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_after(20,30)
    actual=new_linked.head.next.next.value
    expect=30
    assert actual==expect

def test_add_after_last():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert_after(1,30)
    actual=new_linked.head.next.next.value
    expect=30
    assert actual==expect


