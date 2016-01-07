/*
HackerRank 30 day Contest
Input Format

First line contains T, number of test cases. Each test case contains an integer age, representing age of the person.

Constraints
1≤T≤4
−5≤age≤30

Output Format

The code that will test your methods is already in the editor. All you have to do is edit the methods given to you in the editor so that they perform correctly as stated above. If your methods are implemented correctly, each testcase will print out either two or three lines.

If the age is less than zero, then your program should print out:

This person is not valid, setting age to 0.
You are young.
You are young.

If the age is equal or greater than 0, then your program should print out two lines. The first line that the program prints out should be the output of amIOld() on the current age. Then, three years pass via yearPasses() and the second line the program prints should be the output of amIOld() after the time has passed.

Sample Input

4
-1
10
16
18

Sample Output

This person is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
*/
using namespace std;
#include <iostream>

class Person{
public:
   int age ;
   Person(int initial_Age);
   void amIOld();
   void yearPasses();
};
Person::Person(int initial_Age){
  // Add some more code to run some checks on initial_Age
    if (initial_Age < 0) {
        printf("This person is not valid, setting age to 0.\n");
        age = 0;
    }
    else
        age = initial_Age;
}
void Person::amIOld(){
    // Do some computations in here and print out the correct statement to the console 
    if (age < 13){
        printf("You are young.\n");
    }
    else if (age >= 13 && age < 18){
        printf("You are a teenager.\n");
    }
    else
        printf("You are old.\n");
}
    
void Person::yearPasses(){
  // Increment the age of the person in here
    age++;
}

int main(){
    int T,age;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>age;
        Person p(age);
        p.amIOld();
        for(int j=0;j<3;j++)
        {
            p.yearPasses();
            
        }
        p.amIOld();
        cout<<"\n";
    }
    return 0;
}
