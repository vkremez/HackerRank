'''
Problem Statement

Let's learn about list comprehensions! You are given three integers X,Y and Z representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of Xi + Yi + Zi is not equal to N. If X=2, the possible values of Xi can be 0, 1 and 2. The same applies to Y and Z.

Input Format

Four integers X,Y,Z and N each on four separate lines, respectively.

Output Format

Print the list in lexicographic increasing order.

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
# Enter your code here. Read input from STDIN. Print output to STDOU
x, y, z, n = [int(input()) for l in range(4)]
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
