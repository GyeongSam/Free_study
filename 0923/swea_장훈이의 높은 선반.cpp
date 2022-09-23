#include <iostream>
#include <algorithm>

int m;

bool comp(int &a, int &b) { return a > b; }

void BT(int sum,int n, int &B,int&N, int s[]) {
	if (sum >= B) {
		if ((sum - B) < m) m = sum - B;
		return;
	}
	else {
		for (int i = n; n < N; ++n) {
			BT(sum + s[n], n + 1, B, N, s);
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N, B;
		m = 1 << 18;
		scanf("%d %d", &N, &B);
		int s[20];
		for (int n = 0; n < N; ++n) scanf("%d",&s[n]);
		std::sort(s, s + N, comp);
		BT(0, 0, B, N, s);
		printf("#%d %d\n", t, m);
	}
}