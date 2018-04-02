#include <bits/stdc++.h>

using namespace std;

int main(){
    int day = 13;
    int month = 9;
    int year;
    cin >> year;
    if(year < 1918)
    {
        // Julian Calendar
        if(year % 4 == 0) day -= 1;
    }
    else if(year > 1918)
    {
        // Gregorian Calendar
        if(year % 400 == 0) day -= 1;
        else if(year % 4 == 0 && year % 100 != 0) day -= 1;
    }
    else
    {
        // Weird Shit
        day = 26;
        month = 9;
    }
    stringstream s;
    s << setw(2) << setfill('0') << day << '.' << setw(2) << setfill('0') << month << '.' << setw(2) << setfill('0') << year;
    cout << s.str();
    return 0;
}

