#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> arr(N);

    for (size_t i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    vector<int> sorted = arr;
    sort(sorted.begin(), sorted.end());
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());

    for (size_t i = 0; i < N; i++)
    {
        cout << lower_bound(sorted.begin(), sorted.end(), arr[i]) - sorted.begin() << " ";
    }
   
    return 0;
}
