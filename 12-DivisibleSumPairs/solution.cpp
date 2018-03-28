#include <bits/stdc++.h>

using namespace std;

int divisibleSumPairs(int n, int k, vector <int> ar) {
    int count = 0;
    for(int i = 0; i < ar.size(); i++)
    {
        for(int j = i + 1; j < ar.size(); j++)
        {
            if((ar[i] + ar[j]) % k == 0) count += 1;
        }
    }
    return count;
}

int main() {
    int n;
    int k;
    cin >> n >> k;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = divisibleSumPairs(n, k, ar);
    cout << result << endl;
    return 0;
}

