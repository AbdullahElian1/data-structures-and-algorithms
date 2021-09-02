import pytest
from hashtable import __version__


def test_version():
    assert __version__ == '0.1.0'


from hashtable.hash_table import *


@pytest.fixture
def test_hashtable():
    test=HashTable()
    test.add("anas",4444)
    test.add("roaa",5555)
    return test


def test_add():
  test=HashTable()
  test.add('ahmad',555)
  assert test.contains('ahmad')==True

def test_hash():
  test=HashTable()
  assert  test.hash("abdullah")==683

def test_find(test_hashtable):
    test=test_hashtable
    assert test.find("anas") == 4444
    assert test.find("roaa")==5555


def test_not_find(test_hashtable):
    test=test_hashtable
    assert test.find("test") == None

def test_contains(test_hashtable):
    test=test_hashtable
    assert test.contains("anas")
    assert test.contains("roaa")








