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

    return 0