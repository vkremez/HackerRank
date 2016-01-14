'''
Input Format

Input is already handled for you by the code pre-filled in the editor. There are 4 lines of input containing first name, last name, phone, and score, respectively.

Constraints 
4≤|first name|,|last name|≤10 
phone contains exactly 7 digits 
1≤score≤100
Output Format

Output is already handled for you by the code pre-filled in the editor. Your output will be correct if your Grade class constructor and calculate method are properly written.

Sample Input

 Heraldo
 Memelli
 8135627
 90
Sample Output

 First Name: Heraldo
 Last Name: Memelli
 Phone: 8135627
 Grade: O
'''

class Student:
    def __init__(self,firstName,lastName,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
    def display(self):
        print "First Name:",self.firstName
        print "Last Name:",self.lastName
        print "Phone:",self.phone

class Grade(Student):   
    def __init__(self,firstName,lastName,phone,score):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
        self.score=score
    def calculate(self):
        if score < 40:
            return "D"
        elif 40 <= score < 60:
            return "B"
        elif 60 <= score < 75:
            return "A"
        elif 75 <= score < 90:
            return "E"
        elif 90 <= score <= 100:
            return "O"
            
firstName=raw_input().strip()
lastName=raw_input().strip()
phone=int(raw_input())
score=int(raw_input())
stu=Grade(firstName,lastName,phone,score)
stu.display()
print "Grade:",stu.calculate()   
