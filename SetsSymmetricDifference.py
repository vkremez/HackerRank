'''
Input Format

The first line of input contains M. The next line contains M space separated integers. The next line contains N. The following line contains N space separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
Concept

If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT    
N = input()    
a=set(map(int,raw_input().split()))
M = input()
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print(n)
