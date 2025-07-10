#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
using namespace std;

#define MOD 10007

int main()
{
    int N;
    cin >> N;

    int dp[1001][10] = {0};

    for (size_t i = 0; i <= 9; i++)
    {
        dp[1][i] = 1;
    }

    for (size_t i = 2; i <= N; i++)
    {
        for (size_t j = 0; j <= 9; j++)
        {
            for (size_t k = 0; k <= j; k++)
            {
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD;
            }
        }
    }

    int rst = 0;
    for (size_t i = 0; i <= 9; i++)
    {
        rst = (rst + dp[N][i]) % MOD;
    }
    cout << rst;

    return 0;
}