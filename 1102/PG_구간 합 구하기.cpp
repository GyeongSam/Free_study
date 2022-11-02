#define _CRT_SECURE_NO_WARNINGS
#include <iostream>


int N, M, K;
int ip[1000000];
int st[2222222] = { 0, };


int makesgt(int n,int l,int r) {

	printf("%d %d %d\n", n, l, r);

	if (l == r) {
		st[n] = ip[l];
		return ip[l];
	}
	int m = (l + r)/2;
	st[n] = makesgt(2 * n, l, m) + makesgt(2 * n + 1, m+1, r);
	return st[n];
}




int main() {
	scanf("%d %d %d", &N, &M, &K);
	for (int n = 0; n < N; ++n) scanf("%d", &ip[n]);
	makesgt(1, 0, 5);
	for (int i = 1; i < N*N; ++i) printf("%d ", st[i]);

}