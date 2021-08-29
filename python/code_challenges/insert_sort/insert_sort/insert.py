def insertionSort(arr):

  for i in range(1,len(arr)):

    j=i-1
    temp=arr[i]

    while j >=0 and temp < arr[j]:
      arr[j+1]=arr[j]
      j=j-1

    arr[j + 1] =temp

  return arr


arr=[1,6,9,33,55,77]

print(insertionSort(arr))
