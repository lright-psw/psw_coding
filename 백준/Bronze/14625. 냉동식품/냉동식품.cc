#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main() {
    int h1, m1, h2, m2, n;
    cin >> h1 >> m1 >> h2 >> m2 >> n;

    int cnt = 0;
    int nh = h1;
    int nm = m1;
    string sn = to_string(n);

    while (true) {
        string s = (nh < 10 ? "0" : "") + to_string(nh) + (nm < 10 ? "0" : "") + to_string(nm);

        if (s.find(sn) != string::npos) {
            cnt++;
        }

        if (nh == h2 && nm == m2) {
            break;
        }

        nm += 1;
        if (nm == 60) {
            nm -= 60;
            nh++;
        }
    }
    cout << cnt;
    return 0;
}
