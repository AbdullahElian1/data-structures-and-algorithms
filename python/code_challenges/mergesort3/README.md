# Merge Sort

## Auther:Abdullah ELian
## contributor :Anas Abu Ghalia
# Challenge Summary

Create function take an array as argument than sort it in Merge Sort.

## Whiteboard Process
![merge_sortion](blog/1.jpg)

## Approach & Efficiency

+ Define function take list.
+ Declare n equal the length of list
+ Let mid half of n
+ Let left the first half and right the rest.
+ Call the function again with left and right
+ Create new function called merge take three argument left, right and the original list
+ Call merge with the left, right and list



## Solution
~~~

def mergesort(arr):
n=len(arr)

if n > 1:
mid =int(n/2)
left =arr[0:mid]
right =arr[mid:n]
# sort the left side
mergesort(left)
# sort the right side
mergesort(right)
# merge the sorted left and right sides together
merge(left, right, arr)


def merge(left, right, arr):
i =0
j =0
k =0

while i < len(left) and j < len(right):
if left[i] <= right[j]:
arr[k] =left[i]
i =i + 1
else:
arr[k] =right[j]
j =j + 1

k =k + 1

if i == len(left):
arr[k]=right[j]
else:
arr[k]=left[i]

~~~

