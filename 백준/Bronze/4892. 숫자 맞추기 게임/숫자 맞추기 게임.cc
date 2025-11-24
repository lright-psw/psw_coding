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
    int i = 1;
    while (1) {
        int rst = 0;

        int n0 = 0;
        cin >> n0;

        if (n0 == 0) {
            break;
        }

        int n1 = n0 * 3;
        int n4 = 0;
        if (n1 % 2 == 0) {
            n4 = n0 / 2;
            cout << i << ". " << "even " << n4 << endl;
        }
        else {
            n4 = (n0-1) / 2;
            cout << i << ". " << "odd " << n4 << endl;
        }
        i++;
    }

    return 0;
}