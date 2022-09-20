#include <iostream>
using namespace std;

int T,tc,N,n;
char c[52];

int main() {
	scanf("%d", &T);
	while (++tc <= T) {
		scanf("%d %s", &N, c);
		printf("#%d ", tc);
		for (int i = 0; i<N; ++i) {
			if (c[i] >= '0' && c[i] <= '9') {
				n = c[i] - '0';
			}
			else n = c[i] - 'A' + 10;

			for (int q = 8; q >= 1; q /= 2) {
				printf("%d", n >= q);
				n %= q;
			}
		}
		printf("\n");

	}
}