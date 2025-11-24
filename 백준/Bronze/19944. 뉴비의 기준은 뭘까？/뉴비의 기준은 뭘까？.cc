#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <string>
#include <queue>
#include <cmath>
using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
       
    int a = 0, b =0;
    cin >> a >> b;

    if (b <=2 && b>0) {
        cout << "NEWBIE!";
    }
    else if (b > 2 && b <= a) {
        cout << "OLDBIE!";
    }
    else {
        cout << "TLE!";
    }

    return 0;
}