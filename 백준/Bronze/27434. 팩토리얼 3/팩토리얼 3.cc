#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

using ll = long long;

const int BLOCK = 13;
const ll BASE = 10000000000000LL; // 10^13

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<ll> result(1, 1);

    for (int i = 2; i <= N; i++)
    {
        ll carry = 0;
        for (int j = 0; j < result.size(); j++)
        {
            result[j] = result[j] * i + carry;
            carry = result[j] / BASE;
            result[j] %= BASE;
        }
        while (carry) {
            result.push_back(carry % BASE);
            carry /= BASE;
        }
    }
    
    printf("%lld", result.back());

    for (int i = result.size() - 2; i >= 0; --i) {
        printf("%013lld", result[i]);
    }
    printf("\n");
    return 0;
}
