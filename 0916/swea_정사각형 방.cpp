#include <iostream>
#define MR 1001
using namespace std;

struct ax {
	int I;
	int J;
};

int room[MR][MR],cnt[MR][MR];
int ans_cnt,ans_i;
ax order[1002001];
ax ax_sub;
int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };


int main(){
	int T,N;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		ans_cnt = 0;
		ans_i = MR;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &room[i][j]);
				order[N*N-room[i][j]] = { i,j };
			}
		}
		/*for (int i = 1; i <= N * N; ++i) {
			printf("(%d %d) ", order[i].I, order[i].J);

		}
		printf("\n");*/

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				cnt[i][j] = 1;
			}
		}
		/*for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				printf("%d ",cnt[i][j]);
			}
			printf("\n");
		}
		printf("\n");*/


		for (int i = 0; i < N*N; ++i) {
			for (int d = 0; d < 4; ++d) {
				ax_sub.I = order[i].I + di[d];
				ax_sub.J = order[i].J + dj[d];
				if (ax_sub.I >= 0 && ax_sub.I <N && ax_sub.J >=0 && ax_sub.J <N ) {
					if (room[order[i].I][order[i].J] == room[ax_sub.I][ax_sub.J] - 1) {
						cnt[order[i].I][order[i].J] = cnt[ax_sub.I][ax_sub.J] + 1;
						
						if (cnt[order[i].I][order[i].J] > ans_cnt) {
							ans_cnt = cnt[order[i].I][order[i].J];
							ans_i = room[order[i].I][order[i].J];
						}
						else if (cnt[order[i].I][order[i].J] == ans_cnt && ans_i> room[order[i].I][order[i].J]) {
							ans_i = room[order[i].I][order[i].J];
						}
					}
				}

			}

		}
		printf("#%d %d %d\n", t, ans_i, ans_cnt);





	}
}