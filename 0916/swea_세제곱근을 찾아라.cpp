#include <stdio.h>
int T,i,l,r;
long long N,sub;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%lld", &N);
		l = 1;
		r = 1e6;
		while (l <= r) {
			i = (l + r) / 2;
			sub = (long long)i*i*i;
			if ( sub== N) {
				break;
			}
			if (sub > N) {
				r = i - 1;
			}
			else l = i + 1;

		}
		if ((long long)i*i*i != N) i = -1;
		printf("#%d %d\n", t, i);
		
	}
}