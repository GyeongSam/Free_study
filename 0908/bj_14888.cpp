#include <iostream>
using namespace std;

int N;
int num[12];
int op[4];
int M=-1e10, m=1e10;


void BT(int c) {
	if (c == N) {
		if (num[c-1] > M)M = num[c-1];
		if (num[c-1] < m)m = num[c-1];
	}
	for (int a = 0; a < 4; a++) {

		if (op[a]) {
			op[a]--;
			int sub = num[c];
			if (a == 0) num[c] += num[c - 1];
			else if (a == 1) num[c] = num[c - 1]-num[c];
			else if (a==2) num[c] *= num[c - 1];
			else if (a==3) num[c] = num[c - 1]/num[c];
			BT(c + 1);
			num[c] = sub;
			op[a]++;
		}
	}
}
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}
	for (int j = 0; j < 4; j++) {
		cin >> op[j];
	}
	BT(1);
	cout << M <<"\n"<<m;
}