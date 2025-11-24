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
       
    vector<int> arr(4);
    for (size_t i = 0; i <=2; i += 2)
    {
        cin >> arr[i] >> arr[i + 1];
    }

    int a = 0, b = 0;

    a = arr[0] + arr[2];
    b = arr[1] + arr[3];

    if (a < b) {
        cout << "Hanyang Univ.";
    }
    else if (a > b) {
        cout << "Yongdap";
    }
    else {
        cout << "Either";
    }

    return 0;
}