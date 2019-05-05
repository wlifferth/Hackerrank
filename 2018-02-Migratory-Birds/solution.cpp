#include <bits/stdc++.h>

using namespace std;

int migratoryBirds(int n, vector <int> ar) {
    map<int,int> counts;
    vector<int> ids = {1, 2, 3, 4, 5};
    int max_id;
    int max_count = -1;
    for(auto x : ids) counts[x] = 0;
    for(auto x : ar) counts[x] += 1;
    for(auto x : ids)
    {
        if(counts[x] > max_count)
        {
            max_id = x;
            max_count = counts[x];
        }
    }
    return max_id;
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = migratoryBirds(n, ar);
    cout << result << endl;
    return 0;
}
