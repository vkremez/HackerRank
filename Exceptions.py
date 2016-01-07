''''
Task

You are given two values a and b. 
Your task is to do integer division and print a/b.

Input Format

First line contains, number of testcases T. 
Next T line contains, space separated values of a and b.

Constraints

0<T<10
Output Format

Print value of a/b. 
In case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note: 
For integer division in Python 3 use //.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(0, int(raw_input())+1):
    M = raw_input()
    try:
        print(int(M[0]) / int(M[2]))
    except ZeroDivisionError as e:
        print "Error Code:" , e
    except ValueError as e:
        print "Error Code:" , e

