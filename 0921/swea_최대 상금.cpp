#include <iostream>


int N,n,x,MAX;
int num[6];

void swap(int *a, int*b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void BT(int n) {
	if (n == 0) {
		int sub=0;
		int q = 1;
		for (int i = 1; i < x; ++i) {
			q *= 10;
		}
		for (int i = 0; i < x; ++i) {
			sub += num[i] * q;
			q /= 10;
		}
		if (sub > MAX) MAX = sub;
	}

	else {
		for (int i = 0; i < x-1; ++i) {
			for (int j = i + 1; j < x; ++j) {
				swap(&num[i], &num[j]);
				BT(n - 1);
				swap(&num[i], &num[j]);
			}
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t=1;t<=T;++t)
	{
		scanf("%d %d", &N, &n);
		x = 0;
		MAX = 0;
		int c = 10;
		while (c < N) c *= 10;
		c /= 10;

		for (int i = c; i >= 1; i /= 10) {
			num[x++] = N / i;
			N %= i;
		}
		BT(n);

		printf("#%d %d\n", t, MAX);
	}

}