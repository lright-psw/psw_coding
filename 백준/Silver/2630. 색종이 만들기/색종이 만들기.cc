#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

int paper[128][128];
int white = 0, blue = 0;

void divide(int y, int x, int size) {
	int color = paper[y][x];
	bool all_same = true;

	for (size_t i = y; i < y+size; i++)
	{
		for (size_t j = x;  j < x+size;  j++)
		{
			if (paper[i][j] != color) {
				all_same = false;
				break;
			}
		}
		if (!all_same)
			break;
	}
	
	if (all_same) {
		if (color == 0)
			white += 1;
		else
			blue += 1;
	}
	else {
		int half = size / 2;
		divide(y, x, half);
		divide(y, x + half, half);
		divide(y + half, x, half);
		divide(y + half, x + half, half);
	}
}

int main() {
	int n = 0;
	cin >> n;

	for (size_t i = 0; i < n; i++)
	{
		for (size_t j = 0; j < n; j++)
		{
			cin >> paper[i][j];
		}
	}
	divide(0, 0, n);

	cout << white << '\n' << blue;

	return 0;
}
