#include <iostream>

int N, MIN, cost[16][16];
bool choice[16];

void BT(int n, int sum) {
	if (n == N) {
		if (sum < MIN) {
			MIN = sum;
		}
	}
	else if (sum > MIN) return;
	for (int i = 0; i < N; ++i) {
		if (!choice[i]) {
			choice[i] = 1;
			BT(n + 1, sum + cost[n][i]);
			choice[i] = 0;
		}
	}
}
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		MIN = 1 << 15;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &cost[i][j]);
			}
		}
		BT(0, 0);
		printf("#%d %d\n", t, MIN);
	}

}