#include <iostream>
#include <algorithm>
using namespace std;

int N = 0;


int dsf(int num)
{
	int tmp = num;
	if (num * 10 + 4 <= N)
		tmp = dsf(num * 10 + 4);
	if (num * 10 + 7 <= N)
		tmp = max(tmp, dsf(num * 10 + 7));
	return tmp;
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int max_value = 0;
	cin >> N;
	max_value = dsf(0);

	cout << max_value << endl;
}