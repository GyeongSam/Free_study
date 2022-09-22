#include <iostream>
#include <algorithm>


bool comp(int a, int b) {
	return a > b;
}


int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		int N, M,sum=0;
		int ct[101], tr[101];
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i) scanf("%d", &ct[i]);
		for (int i = 0; i < M; ++i) scanf("%d", &tr[i]);
		std::sort(ct, ct + N,comp);
		std::sort(tr, tr + M,comp);
		int j = 0;
		for (int i = 0; i < N; ++i) {
			if (j >= M) break;
			if (ct[i] <= tr[j]) {
				sum += ct[i];
				++j;
			}

		}
		printf("#%d %d\n", tc, sum);

	}
}
