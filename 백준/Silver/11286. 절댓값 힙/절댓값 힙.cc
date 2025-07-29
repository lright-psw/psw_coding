#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int N;

struct compare
{
    bool operator()(const int& a, const int& b) const{
        if (abs(a) == abs(b)) // 만약 a가 b랑 절대값이 같으면 작은거 ㄱㄱ
            return a > b;
        return abs(a) > abs(b);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;

    priority_queue<int, vector<int>, compare> pq;

    for (int i = 0; i < N; i++)
    {
        int x;
        cin >> x;

        if (x == 0) {
            if (pq.empty()) {
                cout << "0\n";
            }
            else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else {
            pq.push(x);
        }
    }
    
    return 0;
}
