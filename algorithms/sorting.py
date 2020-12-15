
def insertion_sort(arr):
    """
    Returns the list 'arr' sorted in nondecreasing order in O(n^2) time.
    """

    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


def merge_sort(arr):
    """
    Returns the list 'arr' sorted in nondecreasing order in O(nlogn) time.
    """
    r = len(arr)
    if 1 < len(arr):
        q = int(r/2)
        L = merge_sort(arr[0:q])
        R = merge_sort(arr[q:])

        print(L,R)
        i,j,k = 0,0,0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i+1
                k = k+1
            elif R[j] < L[i]:
                arr[k] = R[j]
                j = j+1
                k = k+1
        if i >= len(L):
            while j < len(R):
                arr[k] = R[j]
                j = j+1
                k = k+1
        elif j >= len(R):
            while i < len(L):
                arr[k] = L[i]
                i = i+1
                k = k+1

    print(arr,'\n')
    return arr

        


if __name__ == '__main__':
    arr = [36, 96, 82, 27, 13, 20, 2, 99, 39, 6, 51, 22, 21, 38, 37, 24, 83, 49, 86, 9, 93, 75, 14, 26, 35, 65, 29, 45, 77, 52, 31, 84]

    #print([arr[i] for i in [1,2,6,12,30]])
    print(insertion_sort(arr))

    print(merge_sort(arr))