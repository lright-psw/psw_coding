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
       
    vector<int> arr(5);
    memset(0, arr.size(), 0);
    int a = 0, b = 0, c = 0;
    int rst = 0;

    int n = 0;
    cin >> n;

    //국어, 수학, 영어, 탐구, 제2외국어
    for (size_t i = 0; i <n; i++)
    {
        cin >> arr[i];
    }

    if (arr[0] > arr[2]) {
        a = arr[0] - arr[2];
        a *= 508;
    }
    else {
        a = arr[2] - arr[0];
        a *= 108;
    }

    if (arr[1] > arr[3]) {
        b = arr[1] - arr[3];
        b *= 212;
    }
    else {
        b = arr[3] - arr[1];
        b *= 305;
    }

    if (arr[4] > 0) {
        c = arr[4] * 707;
    }

    cout << (a + b + c) * 4763;


    return 0;
}