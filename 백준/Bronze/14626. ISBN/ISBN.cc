#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string isbn;
    cin >> isbn;
    
    int missing_num = -1;
    int sum = 0;

    for (int i = 0; i < 13; i++)
    {
        if (isbn[i] == '*') {
            missing_num = i;
            continue;
        }

        int num = isbn[i] - '0';

        if (i % 2 == 0) {
            sum += num;
        }
        else {
            sum += num * 3;
        }
    }
    
    for (int i = 0; i <= 9; i++) {
        int temp_sum = sum;

        if (missing_num % 2 == 0) {
            temp_sum += i;
        }
        else {
            temp_sum += i * 3;
        }

        if (temp_sum % 10 == 0) {
            cout << i << '\n';
            break;
        }
    }

    return 0;
}
