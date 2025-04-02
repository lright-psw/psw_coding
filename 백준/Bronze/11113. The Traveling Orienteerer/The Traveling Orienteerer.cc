#ifndef _CRT_SECURE_NO_WARNIGS
#define _CRT_SECURE_NO_WARNIGS
#endif

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <deque>
#include <cmath>
using namespace std;

struct POINT {
	double x, y;
};




int main() {
	ios::sync_with_stdio(false);
	cout.tie(nullptr);
	cin.tie(nullptr);

	int n = 0;
	cin >> n;
	vector<POINT> points(n);

	for (int i = 0; i < n; i++)
	{
		cin >> points[i].x >> points[i].y;
	}

	int m, p = 0;
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> p;
		vector<int> route(p);
		for (int j = 0; j < p; j++)
		{
			cin >> route[j];
		}

		double totalDist = 0.0;
		for (int j = 0; j < p-1; j++)
		{
			POINT a = points[route[j]];
			POINT b = points[route[(j + 1)]];
			double dx = a.x - b.x;
			double dy = a.y - b.y;
			totalDist += sqrt(dx * dx + dy * dy);
		}
		cout << (int)round(totalDist) << endl;
	}
	return 0;
}