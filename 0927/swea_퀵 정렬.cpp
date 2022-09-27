#include <iostream>

int N, list[1000000];

void swap(int a, int b) {
	int temp = list[a];
	list[a] = list[b];
	list[b] = temp;
}

void quick_sort(int start, int end) {
	if (start >= end) return;
	int fv = start;
	int l = start;
	int r = end+1;
	while (1) {
		while (l<end && list[fv] > list[++l]);
		while (r>start && list[fv] < list[--r]);
		if (l == end || r == start + 1 || r<=l) break;
		swap(l, r);
	}
	swap(fv, r);
	quick_sort(start, r - 1);
	quick_sort(r + 1, end);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		for (int n = 0; n < N; ++n) scanf("%d", &list[n]);
		quick_sort(0, N - 1);
		printf("#%d %d\n", t, list[N / 2]);
	}
	
}