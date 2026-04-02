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



def backtracking(dp,A,B, i, j):
    
    ### iterate untill i , j == 0

    if i == 0 or j == 0:
        return ''
    
    if A[i-1] == B[j-1]:
        # recursive call
        result = backtracking(dp,A,B, i-1, j-1)

        return result + A[i-1] ### we return
    
    ## now go left or right depending on the larger value

    if dp[i-1][j] >= dp[i][j-1]:
        return backtracking(dp,A,B, i-1, j)
    else:
        return backtracking(dp,A,B, i, j-1)
    
        ## we chose this value add the character to the substring
        ## we also go diagonal upper left 

    
    ### backtracking helper function to retrieve the string from the final dp array

def hvlcs(K, vals, A, B):
    # Base case
    if K == 0 or A == '' or B == '':
        return 0, ''
    
    # Initilizations
    vals_dict = dict(vals)
    m = len(A)
    n = len(B)
    M = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                M[i][j] = M[i-1][j-1] + vals_dict[A[i-1]]
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])

    # Backtracking
    lcs = backtracking(M,A,B,m,n)

    return M[m][n], lcs
