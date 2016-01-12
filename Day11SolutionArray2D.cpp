/*
Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of −9 to 9.

Constraints 
−9≤A[i][j]≤9 
0≤i,j≤5
Output Format

Print the largest (maximum) hourglass sum found in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

Sample Input A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
*/


#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int hourglass(vector< vector <int> >& arr) {
    // store dimensions of 2D vector 
    int n = arr.size(), o = arr[0].size();
    
    vector<int> ans;
    // i < n - 2 because hourglass seeks
    // 2 below; j < o -2 because 2 to the right
    for (int i = 0; i < n - 2; i++) {
        for (int j = 0; j < o - 2; j++) {
            int sum = 0;
            
            // read current spot and two to the right
            // and the three that are two rows below
            for (int x = j; x <= j + 2; x++) {
                sum += (arr[i][x] + arr[i+2][x]);
            }
            
            // read that element in the middle
            sum += arr[i+1][j+1];
            
            ans.push_back(sum);
        }
    }
    
    return *max_element(ans.begin(), ans.end());
}
int main(){
    vector< vector<int> > arr(6,vector<int>(6));
    for(int arr_i = 0;arr_i < 6;arr_i++){
       for(int arr_j = 0;arr_j < 6;arr_j++){
          cin >> arr[arr_i][arr_j];
       }
    }
    
    cout << hourglass(arr) << endl;
    return 0;
}
