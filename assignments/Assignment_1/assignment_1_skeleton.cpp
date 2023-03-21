// CSCI 411 - Spring 2023
// Assignment 1 Skeleton
// Author: Carter Tillquist
// Feel free to use all, part, or none of this code for the coding problem on assignment 1.

#include <iostream>
#include <vector>
using namespace std;

/**************************************************************************
 * A simple Node struct                                                   *
 * id - int - the id or name of the node                                  *
 * SCC - int - the strongly connected component that this node belongs to *
 * visited - bool - whether or not this node has been visited             *
 * ************************************************************************/
struct Node {
    int id;
    int SCC;
    bool visited;
};

/**************************************************************************************************
 * A simple struct of strongly connected component (SCC) graph nodes                              *
 * id - int - the id or name of the node (this corresponds to the SCC id)                         *
 * size - int - the number of nodes from the original graph that belong to this SCC               *
 * hasInEdges - bool - true if there are edges with end points in this SCC and false otherwise    *
 * hasOutEdges - bool - true if there are edges with start points in this SCC and false otherwise *
 * ************************************************************************************************/
struct SCCNode {
    int id;
    int size;
    bool hasInEdges;
    bool hasOutEdges;
};

/*********************************************************
 * A simple struct to hold the sizes of sets A, B, and C *
 * A - int - the size of set A                           *
 * B - int - the size of set B                           *
 * C - int - the size of set C                           *
 * *******************************************************/
struct Result {
    int A;
    int B;
    int C;
};

/******************************************************************************************************************
 * Given the adjacency list of a graph, generate a new adjacency list with the same nodes but with edges reversed *
 * A - vector<vector<shared_ptr<Node>>> - an adjacency list representation of a graph. Note that A[0] is a list   * 
 *     of all the Nodes in the graph with an additional dummy Node at A[0][0]. As a result, A[i] are the          * 
 *     neighbors of the Node with id i where these ids go from 1 to n, the size of the graph                      *
 * return - vector<vector<shared_ptr<Node>>> - an adjacency list of a new graph equivalent to the original but    *
 *          with edges reversed                                                                                   *
 * ****************************************************************************************************************/
vector<vector<shared_ptr<Node>>> reverseEdges(vector<vector<shared_ptr<Node>>> A){
    //YOUR CODE HERE
}

/********************************************************************************************************
 * A variation of DFS for the first pass over a graph looking for strongly connected components.        *
 * The goal is to fill the vector L with nodes in decreasing order with respect to finishing time       *
 * A - vector<vector<shared_ptr<Node>>> - an adjacency list                                             *
 * v - shared_ptr<Node> - the start node for the DFS                                                    *
 * &L - vector<shared_ptr<Node>> - a list of nodes to be filled in decreasing order with respect to     *
 *      finishing time                                                                                  *
 * ******************************************************************************************************/
void DFSSCC(vector<vector<shared_ptr<Node>>> A, shared_ptr<Node> v, vector<shared_ptr<Node>> &L){
    //YOUR CODE HERE
}

/******************************************************************************************************************
 * A variation of DFS for the second pass over a graph looking for strongly connected components.                 *
 * There are three goals (1) to label nodes with a SCC id (2) to generate nodes of a SCC metagraph (3) and to     *
 * determine which nodes in this metagraph have incoming and outgoing edges.                                      *
 * A - vector<vector<shared_ptr<Node>>> - an adjacency list representing the transpose or edge reverse of the     *
 *     original graph                                                                                             *
 * v - shared_ptr<Node>- the start node for the DFS                                                               *
 * scc - int - the current strongly connected component id                                                        *
 * &SCCs - vector<SCCNode> - the nodes of a SCC metagraph                                                         *
 ******************************************************************************************************************/
void DFSAssign(vector<vector<shared_ptr<Node>>> A, shared_ptr<Node> v, int scc, vector<SCCNode> &SCCs){
    //YOUR CODE HERE
}

/******************************************************************************************************
 * Find the strongly connected components (SCCs) of a graph. The SCC of each Node is added to the SCC *
 * member of the Node struct. In addition, a vector of SCCNode is returned.                           *
 * A - vector<vector<shared_ptr<Node>>> - an adjacency list                                           *
 * return - vector<SCCNode> - a vector of nodes in the SCC metagraph of A                             *
 * ****************************************************************************************************/
vector<SCCNode> SCC(vector<vector<shared_ptr<Node>>> A){
    //YOUR CODE HERE
}

/************************************************************************************************
 * Given the adjacency list representation of a graph, fill and return a Result struct with the *
 * number of nodes that belong to the three sets A, B, and C as described in assignment 1       *
 * A - vector<vector<shared_ptr<Node>>> - an adjacency list                                     *
 * return - Result - a Result struct holding the sizes of sets A, B, and C                      *
 * **********************************************************************************************/
Result getSetSizes(vector<vector<shared_ptr<Node>>> A){
    //YOUR CODE HERE
}

int main(){
    //get the number of nodes and number of edges from cin separated by a space
    cout << "Number of nodes and number of edges: " << endl;
    int n = -1, m = -1;
    cin >> n >> m;

    //add the nodes to an adjacency list
    //note that A[0] is a list of nodes with a dummy node in A[0][0]
    //this means that A[i] is the node with id i where ids start at 1
    vector<vector<shared_ptr<Node>>> A(n+1);
    A[0].push_back(shared_ptr<Node>(new Node()));
    for (int i=1; i<n+1; i++){
        shared_ptr<Node> v = shared_ptr<Node>(new Node());
        v->id = i;
        v->SCC = -1;
        v->visited = false;
        A[0].push_back(v);
    }

    //get edges from cin and add them to the adjacency list
    //the start and end of a single edge are on the same line separated by a space
    cout << "Add " << m << " edges: " << endl;
    int u = -1, v = -1;
    for (int i=0; i<m; i++){
        cin >> u >> v;
        A[u].push_back(A[0][v]);
    }

    //call getSetSizes to determine the size of the sets A, B, and C and print the results
    Result R = getSetSizes(A);
    cout << "|A| = " << R.A << ", |B| = " << R.B << ", |C| = " << R.C;

    return 0;
}
