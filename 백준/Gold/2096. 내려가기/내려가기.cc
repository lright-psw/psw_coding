#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 100000

int N;
int a[3];
int dp_max[3];
int dp_min[3];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    
    for (size_t i = 0; i < 3; i++)
    {
        cin >> a[i];
        dp_max[i] = dp_min[i] = a[i];
    }

    for (size_t i = 1; i < N; i++)
    {
        for (size_t j = 0; j < 3; j++)
        {
            cin >> a[j];
        }

        int max0 = max(dp_max[0], dp_max[1]) + a[0];
        int max1 = max({dp_max[0], dp_max[1], dp_max[2]}) + a[1];
        int max2 = max(dp_max[1], dp_max[2]) + a[2];

        int min0 = min(dp_min[0], dp_min[1]) + a[0];
        int min1 = min({ dp_min[0], dp_min[1], dp_min[2] }) + a[1];
        int min2 = min(dp_min[1], dp_min[2]) + a[2];

        dp_max[0] = max0;
        dp_max[1] = max1;
        dp_max[2] = max2;

        dp_min[0] = min0;
        dp_min[1] = min1;
        dp_min[2] = min2;
    }

    cout << max({ dp_max[0], dp_max[1], dp_max[2] }) << ' ' << min({ dp_min[0], dp_min[1], dp_min[2] }) << endl;
    return 0;
}
