#include <iostream>

int min,N;

void BT(int i,int cnt,int charge[]) {
	if (i >= N-1) {
		if (cnt < min) min = cnt;
		return;
	}
	else if (cnt > min) return;

	for (int x = i + charge[i]; x >= i + 1; --x) {
		BT(x, cnt + 1, charge);
	}
}
int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		int charge[100];
		min = 1<<11;
		for (int n = 0; n < N-1; ++n) scanf("%d", &charge[n]);
		BT(0, -1, charge);
		printf("#%d %d\n",t,min);
	}
}