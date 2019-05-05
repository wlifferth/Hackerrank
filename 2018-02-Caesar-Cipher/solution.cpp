#include <bits/stdc++.h>

using namespace std;

string caesarCipher(string s, int k) {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for(int i = 0; i < s.size(); i++)
    {
        int afound = alphabet.find(s[i]);
        int uafound = upperAlphabet.find(s[i]);
        if(afound != -1)
        {
            s[i] = alphabet[(afound + k) % alphabet.size()];
        }
        else if(uafound != -1)
        {
            s[i] = upperAlphabet[(uafound + k) % upperAlphabet.size()];
        }
    }
    return s;
}

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int k;
    cin >> k;
    string result = caesarCipher(s, k);
    cout << result << endl;
    return 0;
}

