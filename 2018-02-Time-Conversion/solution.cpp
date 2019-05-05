#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string t) {
    /*
     * Write your code here.
     */
    stringstream ss;
    int h, m, s;
    char ch, aorp;
    ss << t;
    ss >> h >> ch >> m >> ch >> s >> aorp;
    if(aorp == 'P')
    {
        if(h < 12) h += 12;
    }
    else if(h == 12) h = 0;
    ss.str(std::string());
    ss << setw(2) << setfill('0') << h << ':'
        << setw(2) << setfill('0') << m << ':'
        << setw(2) << setfill('0') << s << endl;
    return ss.str();

}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
