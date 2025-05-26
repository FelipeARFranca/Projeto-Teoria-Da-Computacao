def heapify(arr, n, i):

    largest = i

    left = i * 2 + 1

    right = i * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp

        heapify(arr, n, largest)

def buildMaxHeap(arr, n):

    for i in range (n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapSort(arr, n):

    buildMaxHeap(arr, n)

    for i in range (n - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

        heapify(arr, i, 0)

def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()

# main

n = 10 ** 2
arr = [] 

for i in range (n, 0, -1):
    arr.append(i)

heapSort(arr, len(arr))
#printArray(arr)