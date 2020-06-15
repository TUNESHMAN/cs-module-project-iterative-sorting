# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here

    return arr


l = [5, 1, 8, 2, 31, 15, 99, 54, 6, 40]
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # from i=0, compare i and i+1
    # The index with higher value stays on the right, the index with the lower value stays on the left
    # If arr[i] > arr[i+1], swap their position. (arr[i]=arr[i+1] and arr[i+1]= arr[i])
    # If at least one swap, repeat
    # Your code here
    swap = True
    while swap:
        count = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        if count == 0:
            swap = False

    return arr


bubble = bubble_sort(l)
print(bubble)


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
