#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int main() {

    int N, r, c;
    cin >> N >> r >> c;

    int size = 1 << N;
    int ans = 0;

    while (size > 1) {
        size /= 2;
        int q = 0;

        //좌표 확인
        if (r >= size) {
            q += 2;
            r -= size;
        }
        if (c >= size) {
            q += 1;
            c -= size;
        }
        ans += q * size * size;
    }
    cout << ans;
   
    return 0;
}
