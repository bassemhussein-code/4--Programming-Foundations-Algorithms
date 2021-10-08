def swap(A, i, j):
    temp = A[j]
    A[j] = A[i]
    A[i] = temp


def threeWayPartition(A, end):
    start = mid = 0
    pivot = 1

    while mid <= end:
        if A[mid] < pivot:
            swap(A, start, mid)
            start = start + 1
            mid = mid + 1

        elif A[mid] > pivot:
            swap(A, mid, end)
            end = end - 1
        else:
            mid = mid + 1


A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
threeWayPartition(A, len(A) - 1)
print(A)
