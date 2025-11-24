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

    int rst = 0;

    int n = 0;
    cin >> n;

    for (size_t i = 0; i < n; i++)
    {
        rst -= 1;
        int tmp = 0;
        cin >> tmp;
        rst += tmp;
    }
    rst += 1;
    cout << rst;

    return 0;
}