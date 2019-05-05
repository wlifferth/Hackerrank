#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, k, tmp;
    int total = 0;
    int charged;
    vector<int> items = vector<int>();
    
    // Read Input
    cin >> n >> k;
    for(int i; i < n; i++)
    {
        cin >> tmp;
        items.push_back(tmp);
    }
    cin >> charged;

    // Solution
    for(auto x: items) total += x;
    total -= items[k];
    int actual = total / 2; 
    if(charged == actual) cout << "Bon Appetit";
    else cout << charged - actual;
    return 0;
}

