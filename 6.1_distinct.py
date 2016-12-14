"""
Write a function

int solution(int A[], int N);
that, given a zero-indexed array A consisting of N integers, 
returns the number of distinct values in array A.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing 
in array A, namely 1, 2 and 3.

Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N), beyond input storage (not 
counting the storage required for input arguments).
"""   
def solution(A):
    A.sort()
    ln = len(A)
    uniques = []
    for i in xrange(ln):
        uniques_ln = len(uniques)
        if uniques_ln == 0:
            uniques.append(A[i])
        if uniques[uniques_ln-1] != A[i]:
            uniques.append(A[i])
    return len(uniques)