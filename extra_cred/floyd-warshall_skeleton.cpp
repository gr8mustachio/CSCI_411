// CSCI 411 - Spring 2023
// Floyd-Warshall algorithm
// Author: Carter Tillquist
// Feel free to use all, part, or none of this code for the Floyd-Warshall coding problem

#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

/********************************************************************************************************
 * Determine distances between every pair of nodes in a graph using the Floyd-Warshall algorithm        *
 * D - vector<vector<int>> - an incomplete distance matrix where D[i][i] = 0 and D[i][j] = (i,j).weight *
 *                           if (i,j) is an edge in the graph and INT_MAX otherwise                     *
 * return - vector<vector<int>> - a matrix where entry i, j is the shortest path distance from node i   *
 *                                to node j in the graph                                                *
 * ******************************************************************************************************/
vector<vector<int>> floydWarshall(vector<vector<int>> D){
  // YOUR CODE HERE
}

int main(){
  //get the number of nodes and the number of edges in the graph
  int n = -1, m = -1;
  cout << "Enter the number of nodes and the number of edges separated by a space: ";
  cin >> n >> m;

  //fill the matrix D with base case values
  //specifically, D[i][i] = 0 and D[i][j] = (i,j).weight if (i,j) is an edge in the graph and INT_MAX otherwise
  cout << "Enter m edges (u,v) and their weights: " << endl;
  vector<vector<int>> D(n, vector<int>(n, INT_MAX));
  for (int i = 0; i < D.size(); i++){ D[i][i] = 0; }
  for (int x = 0; x < m; x++){
    int i = -1, j = -1, w = -1;
    cin >> i >> j >> w;
    D[i-1][j-1] = w;
  }

  //fill the distance matrix D using the Floyd-Warshall algorithm and print the result
  cout << "The distance matrix for G: " << endl;
  D = floydWarshall(D);
  for (int i = 0; i < D.size(); i++){
    for (int j = 0; j < D[i].size(); j++){
      if (D[i][j] < INT_MAX) { cout << D[i][j] << " "; }
      else{ cout << "INF "; }
    }
    cout << endl;
  }

  return 0;
}

