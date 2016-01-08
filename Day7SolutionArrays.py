'''
Input Format

The first line of input contains N, the number of integers. The next line contains N integers separated by a space.

Constraints

1≤N≤1000
1≤Ai≤10000, where Ai is the ith integer in the array.

Output Format

Print the N integers of the array in the reverse order on a single line separated by a space.

Sample Input

4
1 4 3 2
Sample Output

2 3 4 1
'''

#!/bin/python
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print ' '.join(map(str, arr[::-1]))
