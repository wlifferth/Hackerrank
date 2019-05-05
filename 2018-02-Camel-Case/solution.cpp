#include <bits/stdc++.h>

using namespace std;

int camelcase(string s) {
    int words = 1;
    for(auto x: s)
    {
        if(x < 91) words += 1;
    }
    return words;
}

int main() {
    string s;
    cin >> s;
    int result = camelcase(s);
    cout << result << endl;
    return 0;
}
