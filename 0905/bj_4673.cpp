#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int L[10005]{};
	for (int i = 1; i <= 10000; i++) {
		int j = i;
		while (1) {
			j = j + j % 10 + (j >= 10 ? ((j / 10) % 10) : 0) + (j >= 100 ? ((j / 100) % 10) : 0) + (j >= 1000 ? ((j / 1000) % 10) : 0);
			if (j < 10000) L[j] = 1;
			else break;
		}
	}
	for (int j = 1; j < 10000; j++) {
		if (L[j] == 0) {
			cout << j<<"\n";
		}
	}
}