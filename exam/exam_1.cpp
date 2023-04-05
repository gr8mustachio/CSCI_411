// CSCI 411 - Spring 2023
// Exam 1 Skeleton
// Author: Carter Tillquist
// Feel free to use all, part, or none of this code for the coding problem on Exam 1.

#include <iostream>
#include <vector>
using namespace std;

/***************************************************************************
 * A function to determine whether or not a target value m can be achieved *
 * by adding up a subset of values in a given multiset                     *
 * S - vector<int> - a vector of ints representing a multiset              *
 * m - int - a target                                                      *
 * return - bool - true if m can be achieved and false otherwise           *
 * *************************************************************************/
bool subsetSum(vector<int> S, int m){

  // I HAVE NO CLUE WHY turnin SEG FAULTS BUT THE CODE WORKS IF YOU COMPILE AND RUN IT YOURSELF
  int n = S.size();
  vector<vector<bool> > A(n+1, vector<bool>(m+1,false));
  for(int i = 0; i < A[i].size(); i++) {
    A[i][0] = true;
  }
  for(int i = 1; i < n+1; i++){
    for(int j = 1; j < m+1; j++){
      if(j < S[i-1])
        A[i][j] = A[i-1][j];
      else
        A[i][j] = (A[i-1][j] || A[i-1][j-S[i-1]]);
    }
  }
  return A[n][m];
}

int main(){
  //get the size of the multiset and the target
  cout << "Enter the size of the multiset and a target: ";
  int n = -1, m = -1, num = -1;
  cin >> n >> m;

  //read the elements of the multiset
  cout << "Enter the elements of the multiset: ";
  vector<int> S;
  for (int i = 0; i < n; i++){
    cin >> num;
    S.push_back(num);
  }

  bool result = subsetSum(S, m);
  cout << "The target " << m << " can" << (result ? " " : "not ") << "be achieved" << endl;

  return 0;
}

