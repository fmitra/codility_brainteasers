"""
A zero-indexed array A consisting of N integers is given. Rotation 
of the array means that each element is shifted right by one index, 
and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. 
The goal is to rotate array A K times; that is, each element of A will be 
shifted to the right by K indexes.

Write a function:

struct Results solution(int A[], int N, int K);
that, given a zero-indexed array A consisting of N integers and an 
integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function 
should return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution 
will not be the focus of the assessment.
"""
def solution(A):
    if len(A) == 1:
        return A[0]
    B = sorted(A)
    total = len(B)
    cache = 0

    # Determining non duplicates based on non matching
    # only works if the start of the list or end do not match
    if B[0] != B[1]:
        return B[0]

    if B[total-1] != B[total-2]:
        return B[total-1]

    for i in xrange(total)
        # If the index is odd, the previous value must match because
        # the array is sorted. If it fails to match, the previous index
        # must be the value we're looking for
        if i & 1:
            if B[i] != cache:
                return cache
        else:
            cache = B[i]