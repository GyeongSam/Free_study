#include <iostream>


int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N,ans=0;
		int cafe[20][20];
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &cafe[i][j]);
			}
		}

		for (int d = N - 1; d >= 2; --d) {
			if (ans >= 2 * d) break;

			for (int d1 = 1; d - d1 >= 1; ++d1) {
				
				for (int i = 0; i < N; ++i) {
					if (i + d >= N) continue;
					
					for (int j = 1; j < N - 1; ++j) {
						int c1 = d1, c2 = d - c1, c3 = c1, c4 = c2;
						if (j < c1 || N - j <= c4) continue;
						
						bool cnt[101] = { 0, }, can = 1;
						int I = i, J = j;
						cnt[cafe[I][J]] = 1;
						
						//printf("ÀÌ¹ø¿£(%d,%d)¿¡¼­ %d ¸¸Å­ µ¹¾Æ¿ä\n",i,j,2*d); 
						//printf("c1:%d,c2:%d,c3:%d,c4:%d\n", c1, c2, c3, c4);

						while (c1--) {
							++I; --J;
							//printf("(%d %d):%d °ãÄ§?%d\n", I, J, cafe[I][J], cnt[cafe[I][J]]);
							if (cnt[cafe[I][J]]) { can = 0; break; }
							else cnt[cafe[I][J]] = 1;
						}
						if (!can)continue;
						while (c2--) {
							++I; ++J;
							//printf("(%d %d):%d °ãÄ§?%d\n", I, J, cafe[I][J], cnt[cafe[I][J]]);
							if (cnt[cafe[I][J]]) { can = 0; break; }
							else cnt[cafe[I][J]] = 1;
						}
						if (!can)continue;
						while (c3--) {
							--I; ++J;
							//printf("(%d %d):%d °ãÄ§?%d\n", I, J, cafe[I][J], cnt[cafe[I][J]]);
							if (cnt[cafe[I][J]]) { can = 0; break; }
							else cnt[cafe[I][J]] = 1;
						}
						if (!can)continue;
						while (c4--) {
							--I; --J;
							/*printf("(%d %d):%d °ãÄ§?%d\n", I, J, cafe[I][J], cnt[cafe[I][J]]);*/
							if (cnt[cafe[I][J]] && I != i && J != j) { can = 0; break; }
							else cnt[cafe[I][J]] = 1;
						}
						if (can) ans = 2*d;
					}
				}


			}


		}
		if (!ans) ans = -1;
		printf("#%d %d\n", t, ans);

	}
}