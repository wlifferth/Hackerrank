#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int positives = 0;
    int negatives = 0;
    int zeroes = 0;
    int n;
    int tmp;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> tmp;
        if(tmp > 0) positives++;
        else if(tmp < 0) negatives++;
        else zeroes++;
    }
    cout << static_cast<double>(positives) / static_cast<double>(n) << endl;
    cout << static_cast<double>(negatives) / static_cast<double>(n) << endl;
    cout << static_cast<double>(zeroes) / static_cast<double>(n) << endl;
    return 0;
}
