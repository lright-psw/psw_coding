#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <string>
using namespace std;

#define MAX 100000

int main()
{
    int N;
    cin >> N;
    unordered_map<string, int> m;
    string name;

    for (size_t i = 0; i < N; i++)
    {
        cin >> name;
        m[name] += 1;
    }

    for (size_t i = 0; i < N-1; i++)
    {
        cin >> name;
        m[name]--;
    }

    for (const auto& now : m) {
        if (now.second > 0) {
            cout << now.first << "\n";
        }
    }

    return 0;
}