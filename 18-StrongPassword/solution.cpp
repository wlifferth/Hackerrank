#include <bits/stdc++.h>

using namespace std;

int minimumNumber(int n, string password) {
    bool dFlag = false;
    bool lFlag = false;
    bool uFlag = false;
    bool sFlag = false;
    string special_characters = "!@#$%^&*()-+";
    for(auto c: password)
    {
        if(c >= 48 && c < 58) dFlag = true;
        else if(c >= 97 && c < 123) lFlag = true;
        else if(c >= 65 && c < 91) uFlag = true;
        else if(special_characters.find(c) != -1) sFlag = true;
    }
    int needed_flags = 4 - dFlag - lFlag - uFlag - sFlag;
    int needed_chars = 6 - n;
    if(needed_flags <= 0 && needed_chars <= 0) return 0;
    if(needed_flags > needed_chars) return needed_flags;
    else return needed_chars;
}

int main() {
    int n;
    cin >> n;
    string password;
    cin >> password;
    int answer = minimumNumber(n, password);
    cout << answer << endl;
    return 0;
}

