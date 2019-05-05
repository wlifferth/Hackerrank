#include <bits/stdc++.h>
using namespace std;

string reduce(string x);

int main() {
    string x;
    string r = "";
    bool unchanged = false;
    cin >> x;
    while(!unchanged)
    {
        r = reduce(x);
        if(x == r) unchanged = true;
        else
        {
            x = r;
            r = "";
        }
    }
    if(x == "") cout << "Empty String";
    else cout << x;
    return 0;
}

string reduce(string x)
{   
    string r = "";
    for(int i; i < x.size(); i++)
    {
        if(i < x.size() - 1)
        {
            if(x[i] == x[i + 1])
            {
                i++;
            }
            else
            {
                r += x[i];
            }
        }
        else
        {
            r += x[i];
        }
    }
    return r;
}
