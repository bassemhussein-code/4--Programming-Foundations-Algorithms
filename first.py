

def partition(A):

    j = 0
    pivot = 0

    for i in range(len(A)):
        if A[i] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

            j += 1

    return j


def rearrange(A):

    p = partition(A)

    n = 0

    while len(A) > p > n:

        temp = A[p]
        A[p] = A[n]
        A[n] = temp

        n += 2
        p += 1


A = [9, -3, 5, -2, -8, -6, 1, 3]
rearrange(A)

print(A)


def insertionSort(A):

    for i in range(1, len(A)):

        Value = A[i]

        j = i

        while j > 0 and A[j-1] > Value:

            A[j] = A[j-1]

            j = j-1

        A[j] = Value


A = [3, 8, 5, 4, 1, 9, -2]

insertionSort(A)

print(A)
