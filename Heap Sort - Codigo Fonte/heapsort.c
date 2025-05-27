#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void heapify(int arr[], int n, int i);
void buildMaxHeap (int arr[], int n);
void heapSort(int arr[], int n);

void printArray(int arr[], int n);

int main(void)
{
    //int n = pow(10, 6);
    //int n = pow(10, 6)/2;
    //int n = pow(10, 5);
    //int n = pow(10, 5)/2;
    //int n = pow(10, 4);
    //int n = pow(10, 4)/2;
    //int n = pow(10, 3);
    //int n = pow(10, 3)/2;
    int n = pow(10, 2);

    int *arr = (int *)malloc(n * sizeof(int));
    for (int i = n - 1; i >= 0; i--)
    {
        arr[i] = i + 1;
    }

    heapSort(arr, n);

    //printArray(arr, n);

    return 0;
}

void heapify(int arr[], int n, int i)
{
    int largest = i;

    int left = 2 * i + 1;

    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
    {
        largest = left;
    }

    if (right < n && arr[right] > arr[largest])
    {
        largest = right;
    }

    if (largest != i)
    {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        heapify(arr, n, largest);
    }
}

void buildMaxHeap (int arr[], int n)
{
    for(int i = n / 2 - 1; i >= 0; i--)
    {
        heapify(arr, n, i);
    }
}

void heapSort(int arr[], int n)
{
    buildMaxHeap(arr, n);

    for (int i = n -1; i > 0; i--)
    {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] =  temp;

        heapify(arr, i, 0);
    }
}

void printArray(int arr[], int n) 
{
    for (int i = 0; i < n; i++) 
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
