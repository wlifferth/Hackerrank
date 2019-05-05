#include <bits/stdc++.h>

using namespace std;

int solve(int n, vector < int > s, int d, int m){
    // Complete this function
    int size = 0;
    int total = 0;
    int count = 0;
    for(int i = 0; i < n; i++)
    {
        if(size < m)
        {
            size += 1;
            total += s[i];
            if(size == m && total == d) count += 1;
        }
        else
        {
            total -= s[i - m];
            total += s[i];
            if(total == d) count += 1;
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    vector<int> s(n);
    for(int s_i = 0; s_i < n; s_i++){
       cin >> s[s_i];
    }
    int d;
    int m;
    cin >> d >> m;
    int result = solve(n, s, d, m);
    cout << result << endl;
    return 0;
}

