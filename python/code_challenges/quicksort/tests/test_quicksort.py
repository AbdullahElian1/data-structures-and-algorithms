from quicksort import __version__
from quicksort.quick import QuickSort

def test_version():
    assert __version__ == '0.1.0'

def test_check_QuickSort():

    arr=[7,8,9,0,4,2]
    actual=QuickSort(arr,0,len(arr)-1)
    expected=[0, 2, 4, 7, 8, 9]

    assert expected==actual
