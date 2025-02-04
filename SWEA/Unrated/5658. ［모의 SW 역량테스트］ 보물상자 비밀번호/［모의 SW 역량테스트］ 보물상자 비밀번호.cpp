#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <climits>
#include <string>
#include <cstring>
using namespace std;

/*
추가 조건!
set 자료형 사용 금지
*/

deque<char> fig;
vector<string> pw;
string s;

// 디버깅 용
void print_pw() {
	for (int i = 0; i < pw.size(); i++)
	{
		cout << pw[i] << " ";
	}
}

void print_fig(int N, int atm) {
	cout << "\n반복" << atm << " : ";
	for (int i = 0; i < N; i++)
	{
		cout << fig[i];
	}
	cout << "\n";
}

// 로직
void parse_num(int N) {
	for (int i = 0; i < N; i += (N/4))
	{
		s.clear();
		for (int j = 0; j < N/4; j++)
		{
			s.push_back(fig[i + j]);
		}
		//cout << "s : " << s <<" |";
		if (pw.size() > 0) {
			for (int j = 0; j < pw.size(); j++)
			{
				if (pw[j] == s) {
					pw.erase(pw.begin() + j);
					break;
				}
			}
		}
		pw.push_back(s);
	}
	//print_pw();
}

void shift_num(int N, int K) {
	for (int i = 0; i < N / 4; i++)
	{
		parse_num(N);
		char tmp = fig.back();
		fig.pop_back();
		fig.push_front(tmp);
		//print_fig(N, i);
	}
}


int main() {
	int T = 0;
	cin >> T;
	int N, K, rst;
	for (int t = 1; t <= T; t++) {
		rst = 0;
		pw.clear();
		fig.clear();
		cin >> N >> K;
		for (int i = 0; i < N; i++)
		{
			char c;
			cin >> c;
			fig.push_back(c);
		}
		shift_num(N, K);
		sort(pw.begin(), pw.end(),greater<string>());
		//print_pw();
		//cout << pw[K - 1] << "\n";
		for (char c : pw[K-1]) {
			int v;
			if (c >= '0' &&c <= '9') {
				v = c - '0';
			}
			else if(c >= 'A' &&c <= 'Z') {
				v = c - 'A' + 10;
			}
			rst = rst * 16 + v;
		}
		cout << "#" << t << " " << rst << "\n";
	}
	return 0;
}