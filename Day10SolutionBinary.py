'''
Input Format

The first line contains a single integer, T, the number of test cases. The T subsequent lines of test cases each contain a single value, n, the base 10 positive integer to be converted.

Constraints 
1≤T≤1000 
1≤n≤231

Output Format

For each test case, print the value of n in binary on a new line.

Sample Input

2
4
5
Sample Output

100
101
Explanation

Test Case 0: n=4 evaluates to 1×22+0×21+0×20=1×4+0+0=100. 
Test Case 1: n=5 evaluates to 1×22+0×21+1×20=1×4+0+1×1=101.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
for x in range(input()):
    print bin(input())[2:]
