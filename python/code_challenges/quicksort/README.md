# Quick Sort

## Auther:Abdullah ELian
## contributor :Anas Abu Ghalia
### Create function take list as argument then sort it in Quick sort.

## Whiteboard Process
![Image of Yaktocat](./blog/quick.jpg)


## Solution
~~~
def QuickSort(arr, left, right):
if left < right:

position = Partition(arr, left, right)

QuickSort(arr, left, position - 1)

QuickSort(arr, position + 1, right)


def Partition(arr, left, right):

pivot = arr[right] # 16
low = left - 1

for i in range(left,right):

if arr[i] <= pivot :

low += 1

# print(low)
Swap(arr, i, low)

# print(low)
# print(arr)

Swap(arr, right, low + 1)

return low + 1

def Swap(arr, i, low):
temp = arr[i]

arr[i] = arr[low]
arr[low] = temp
~~~

