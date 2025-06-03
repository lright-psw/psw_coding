#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

vector<string> split(string& s, char delimeter) {
	vector<string> result;
	string token;
	stringstream ss(s);
	while (getline(ss, token, delimeter)) {
		result.push_back(token);
	}
	return result;
}

int sum_of_string(string& s) {
	vector<string> nums = split(s, '+');
	int sum = 0;
	for (const string& num : nums) {
		sum += stoi(num);
	}
	return sum;
}

int main() {
	string s;
	cin >> s;

	vector<string> parts = split(s, '-');

	int result = sum_of_string(parts[0]);

	for (auto i = 1; i < parts.size(); i++) {
		result -= sum_of_string(parts[i]);
	}
	cout << result << '\n';
	return 0;
}
