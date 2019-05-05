#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);
int min(vector<int>);
int max(vector<int>);
bool above(vector<int>, int);
bool below(vector<int>, int);

/*
 * Complete the getTotalX function below.
 */
int getTotalX(vector<int> a, vector<int> b) {
    int start = max(a);
    int stop = min(b) + 1;
    int inc = min(a);
    int count = 0;
    for(int i = start; i < stop; i += inc)
    {
        if(above(a, i) && below(b, i)) count += 1; 
    }
    return count;
}

bool above(vector<int> a, int i)
{
    for(auto ai: a)
    {
        if(i % ai != 0) return false;
    }
    return true;
}

bool below(vector<int> b, int i)
{
    for(auto bi: b)
    {
        if(bi % i != 0) return false;
    }
    return true;
}

int min(vector<int> x)
{
    int current_min = x[0];
    for(auto xi: x)
    {
        if(xi < current_min) current_min = xi;
    }
    return current_min;
}

int max(vector<int> x)
{
    int current_max = x[0];
    for(auto xi: x)
    {
        if(xi > current_max) current_max = xi;
    }
    return current_max;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split_string(a_temp_temp);

    vector<int> a(n);

    for (int a_itr = 0; a_itr < n; a_itr++) {
        int a_item = stoi(a_temp[a_itr]);

        a[a_itr] = a_item;
    }

    string b_temp_temp;
    getline(cin, b_temp_temp);

    vector<string> b_temp = split_string(b_temp_temp);

    vector<int> b(m);

    for (int b_itr = 0; b_itr < m; b_itr++) {
        int b_item = stoi(b_temp[b_itr]);

        b[b_itr] = b_item;
    }

    int total = getTotalX(a, b);

    fout << total << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
            return x == y and x == ' ';
            });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

