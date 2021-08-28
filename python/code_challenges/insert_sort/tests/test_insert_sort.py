# import pytest
from insert_sort import __version__
from insert_sort.insert import *


def test_version():
    assert __version__ == '0.1.0'


def test_check_insertionsort():

    arr=[7,8,9,0,4,2]
    actual=insertionSort(arr)
    expected=[0, 2, 4, 7, 8, 9]

    assert expected==actual


