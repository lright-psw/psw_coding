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
    
    int n = 0;
    cin >> n;

    string str;
    cin >> str;

    long long rst = 0;
    string tmp = "";

    for (auto s : str) {
        if ('0' <= s && '9' >= s) {
            tmp += s;
        }
        else {
            if (!tmp.empty()) {
                rst += stoll(tmp);
                tmp = "";
            }
        }
    }

    if (!tmp.empty()) {
        rst += stoll(tmp);
    }

    cout << rst;

    return 0;
}