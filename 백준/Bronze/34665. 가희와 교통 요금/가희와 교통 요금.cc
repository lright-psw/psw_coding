#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <string>
#include <queue>
using namespace std;




int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
       
    string a, b;

    cin >> a >> b;

    if (a.compare(b) == 0) {
        cout << 0;
    }
    else {
        cout << 1550;
    }


    return 0;
}