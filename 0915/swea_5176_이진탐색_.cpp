#include <stdio.h>

int tree[1001];
int T,N,cnt;

void tr(int i) {
	if (i > N) {
		return;
	}
	tr(2 * i);
	tree[i] = ++cnt;
	tr(2 * i + 1);
}
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		cnt = 0;
		scanf("%d", &N);
		tr(1);
		printf("#%d %d %d\n", t, tree[1], tree[N / 2]);
	}
}
