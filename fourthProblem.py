''' a problem consists of a  binary list .. you have to sort it .. zeros first.. .then ones


  and you  need to print all zeros you find ,, in this array ..'''


''' first count the zeros ..
put them in the biginnnig of the array ...
then looop from the rest index .. to the last of the array ..
to put ones in them '''


def sort(A):
    zeros = A.count(0)
    k = 0
    while zeros:
        A[k] = 0
        zeros = zeros-1
        k = k + 1

    for n in range(k, len(A)):
        A[n] = 1


A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]

# sort(A)

# print(A)


def sortTwo(A):
    k = 0

    for i in range(len(A)):
        if A[i] == 0:
            A[k] = 0
            k = k + 1

    for i in range(k, len(A)):
        A[i] = 1


# sortTwo(A)
# print(A)


def sortThree(A):

    pivot = 1
    j = 0

    for i in range(len(A)):
        if A[i] < pivot:
            swap(A, i, j)
            j = j + 1


def swap(A, i, j):
    temp = A[j]
    A[j] = A[i]
    A[i] = temp


sort(A)
print(A)
