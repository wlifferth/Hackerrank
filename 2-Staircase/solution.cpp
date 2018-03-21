#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the staircase function below.
 */
void staircase(int n) {
    /*
     * Write your code here.
     */
    int spaces;
    int hashes;
    for(int i = 0; i < n; i++)
    {
        spaces = n - i - 1;
        hashes = n - spaces;
        for(int j = 0; j < spaces; j++) cout << ' ';
        for(int j = 0; j < hashes; j++) cout << '#';
        cout << endl;
    }
    return;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}

