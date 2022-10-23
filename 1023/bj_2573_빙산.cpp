#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#define F(x,X) for (int x=0;x<X;++x)

struct Q {
	int i, j;
};

int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };
int field[300][300];
int melting[300][300]={0,};
int N, M;
Q temp[10001];


int main() {
	scanf("%d %d", &N, &M);
	F(i, N) F(j, M) scanf("%d", &field[i][j]);
	F(i, N) F(j, M) {
		if (field[i][j]) {
			F(d, 4) {
				int ni = i + di[d], nj = j + dj[d];
				if ( 0<=ni && ni<N && nj>=0 && nj<M && !field[ni][nj]) melting[i][j]++;
			}
		}
	}
	int t=0;
	while (1) {
		int pt = 0;
		++t;
		F(i, N) F(j, M) {
			if (field[i][j]) {
				field[i][j] -= melting[i][j];
				if (field[i][j] <= 0) {
					field[i][j] = 0;
					temp[pt++] = { i,j };
				}
			}
		}

		F(q, pt) {
			F(d, 4) {
				int ni = temp[q].i + di[d], nj = temp[q].j + dj[d];
				if (0 <= ni && ni < N && nj >= 0 && nj < M) melting[ni][nj]++;
			}	
		}



	}



	F(i, N) { F(j, M) printf("%d ", field[i][j]); printf("\n"); } printf("\n");
	F(i, N) { F(j, M) printf("%d ", melting[i][j]); printf("\n"); } printf("\n");

}