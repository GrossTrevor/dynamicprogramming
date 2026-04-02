"""
Highest Value Longest Common Sequence Algorithm

Input Format:
K
x1 v1
x2 v2
...
xK vK
A
B

K is the number of characters in the alphabet.
Each of the next K lines contains a character and its value.
A is the first string.
B is the second string.

Output Format:
Single integer: the maximum value of a common subsequence of A and B.
One optimal common subsequence that achieves this value, on the next line.
"""

def hvlcs(K, vals, A, B):
    # Base case
    if K == 0 or A == '' or B == '':
        return 0, ''
    
    # Initilizations
    vals_dict = dict(vals)
    m = len(A)
    n = len(B)
    M = [[0] * (n + 1) for _ in range(m + 1)]

    # Memoization
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                M[i][j] = M[i-1][j-1] + vals_dict[A[i-1]]
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])

    # Backtracking
    lcs = ''

    return M[m][n], lcs
