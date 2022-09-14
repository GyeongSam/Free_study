#include <iostream>
#include <vector>

using namespace std;

int T, N, K, sub, ans;
int V[1001], R[100001];


void BT(int n, int value) {
	for (int i = 1; i <= N; ++i) {
		if (R[i] == n) {
			cout << i << "속으로 들어감 \n";
			BT(i, value + V[i]);
			
			return;
		}
	}
	cout << value <<"\n";
}


int main() {
	cin >> T;
	while (T--) {
		cin >> N >> K;
		for (int i = 1; i <= N; ++i) {
			cin >> V[i];
		}
		for (int i = 1; i <= K; ++i) {
			cin >> sub >> R[i];
		}
	}
	for (int i = 1; i <= K; ++i) {
		cout << R[i] << " ";
	}
	cout << "\n";
	cin >> ans;
	BT(ans, 0);
}