#include <iostream>
#include <map>
#include <string>

using namespace std;


int main() {
	int N, M;
	string name;
	cin >> N >> M;
	map<int,string> NumToName;
	map<string, int> NameToNum;

	for (int i = 1; i <= N; i++) {
		cin >> name;
		NumToName[i] = name;
		NameToNum[name] = i;
	}
	string pk;
	for (int i = 0; i < M; i++) {
		cin >> pk;
		if ('0' <= pk[0] && pk[0] <= '9') {
			cout << NumToName[stoi(pk)] << "\n";
		}
		else cout << NameToNum[pk] << "\n";
	}
}