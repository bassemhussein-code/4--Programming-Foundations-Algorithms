def findMaximumLenSublist(A, S):

    length = 0

    end_index = -1
    for i in range(len(A)):

        sum = 0
        for j in range(i, len(A)):

            sum += A[j]

            if sum == S:
                if length < j - i + 1:
                    length = j - i + 1
                    end_index = j

    print((end_index - length + 1, end_index))


A = [5, 6, -5, 5, 3, 5, 3, -2, 0]
sum = 8

findMaximumLenSublist(A, sum)
