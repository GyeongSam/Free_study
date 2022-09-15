#include <stdio.h>

int main() {
	int T, n, N,sub;
	int L[1001];
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		sub = 2;
		scanf("%d", &N);
		L[1] = (N + 2) / 2;
		n = (N + 3) /4;
		for (int i = 1; i < N; i++) {
			if (i == sub) { n = (n + 1) / 2; sub *= 2; }
			L[2 * i] = L[i] - n;
			L[2 * i + 1] = L[i] + n;
		}
		for (int i = 1; i < N; i++) {
			printf("%d  ", L[i]);
		}

		printf("#%d %d %d", t, L[1], L[N/2]);
	}
}