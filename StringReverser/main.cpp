#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    cout << "Input Reverser";
    string s;
    while(cout << "\n>>>", getline(cin, s))
        for_each(s.rbegin(), s.rend(), [&](auto it){cout << it;});
}
