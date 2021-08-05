import pytest
from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import Stack,Queue,Node


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

# def test_empty_stack():
#     assert Stack()

def test_has_one_node():
    test=Stack()
    test.push(1)
    expected=1
    actual=test.peek()
    assert expected==actual

def test_insert_more_nodes():
    test=Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    expected=3
    actual=test.__len__()
    assert expected==actual

def test_remove_node():
    test=Stack()
    test.push(1)
    test.push(2)
    test.push(2)
    test.pop()
    expected=2
    actual=test.peek()
    assert expected==actual

def test_stack_is_empty():
  test = Stack()
  assert test.is_empty()

def test_stack_not_empty():
  test = Stack()
  test.push(1)
  assert not test.is_empty()

def test_is_empty_for_peek_and_pop():
    test=Stack()
    with pytest.raises(Exception, match="empty stack"):
         test.peek()
         test.pop()





def test_has_one_node_queueu():
    test=Queue()
    test.enqueue(1)
    expected=1
    actual=test.peek()
    assert expected==actual

def test_insert_more_nodes_queueu():
    test=Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    expected=3
    actual=test.__len__()
    assert expected==actual

def test_remove_node_queueu():
    test=Queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(2)
    test.dequeue()
    expected=2
    actual=test.peek()
    assert expected==actual

def test_stack_is_empty_queueu():
  test = Queue()
  assert test.is_empty()

def test_stack_not_empty_queueu():
  test = Queue()
  test.enqueue(1)
  assert not test.is_empty()

def test_is_empty_for_peek_and_pop_queueu():
    test=Queue()
    with pytest.raises(Exception, match="empty equeue"):
         test.peek()
         test.dequeue()


