#include <iostream>
#define F(x,s,e) for(int x=s;x<=e;++x)
#define F_(x,s,e) for(int x=e;x>=s;--x)

int N, MAX=0;

void dfs(int (*board)[22],int n) {
	if (n == 5) return;

	int new_board[22][22];

	F(i, 0, N + 2) F(j, 0, N + 2) new_board[i][j] = board[i][j];
	F_(i, 1, N) {
		F(j, 1, N) {
			if (new_board[i][j]) {
				int ai = i;
				while (!new_board[ai + 1][j]) ++ai;
				

				if (new_board[ai + 1][j] == new_board[i][j]) {
					new_board[ai + 1][j] += new_board[i][j];
					new_board[i][j] = 0;
					if (new_board[ai + 1][j] > MAX) MAX = new_board[ai + 1][j];
				}
				else if (ai == i)continue;
				else {
					new_board[ai][j] = new_board[i][j];
					new_board[i][j] = 0;
				}
			}
		}
	}

	dfs(new_board, n + 1);

	F(i, 0, N + 2) F(j, 0, N + 2) new_board[i][j] = board[i][j];
	F_(j, 1, N) {
		F(i, 1, N) {
			if (new_board[i][j]) {
				int aj = j;
				while (!new_board[i][aj + 1]) ++aj;
				if (new_board[i][aj + 1] == new_board[i][j]) {
					new_board[i][aj + 1] += new_board[i][j];	
					new_board[i][j] = 0;

					if (new_board[i][aj + 1] > MAX) MAX = new_board[i][aj + 1];
				}
				else if (aj == j)continue;
				else {
					new_board[i][aj] = new_board[i][j];
					new_board[i][j] = 0;
				}
			}
		}
	}
	dfs(new_board, n + 1);
	F(i, 0, N + 2) F(j, 0, N + 2) new_board[i][j] = board[i][j];
	F(i, 1, N) {
		F(j, 1, N) {
			if (new_board[i][j]) {
				int ai = i;
				while (!new_board[ai - 1][j]) --ai;
				if ((ai + 1) != i && new_board[ai - 1][j] == new_board[i][j]) {
					new_board[ai - 1][j] += new_board[i][j];
					new_board[i][j] = 0;
					if (new_board[ai - 1][j] > MAX) MAX = new_board[ai - 1][j];

				}
				else if (ai == i)continue;
				else {
					new_board[ai][j] = new_board[i][j];
					new_board[i][j] = 0;
				}
			}

		}
	}

	dfs(new_board, n + 1);

	F(i, 0, N + 2) F(j, 0, N + 2) new_board[i][j] = board[i][j];
	F(j, 1, N) {
		F(i, 1, N) {
			if (new_board[i][j]) {
				int aj = j;
				while (!new_board[i][aj - 1]) --aj;
				if (new_board[i][aj - 1] == new_board[i][j]) {
					new_board[i][aj - 1] += new_board[i][j];
					new_board[i][j] = 0;
					if (new_board[i][aj - 1] > MAX) MAX = new_board[i][aj - 1];
				}
				else if (aj == j)continue;
				else {
					new_board[i][aj] = new_board[i][j];
					new_board[i][j] = 0;
				}
			}
		}
	}
	dfs(new_board, n + 1);
}


int main() {
	scanf("%d", &N);
	int fisrt_board[22][22] = { 0, };
	F(i, 0, N + 1) {
		F(j, 0, N + 1) {
			if (i == 0 || i == N + 1 || j == 0 || j == N + 1) {
				fisrt_board[i][j] = -1;
			}
			else {
				scanf("%d", &fisrt_board[i][j]);
				if (fisrt_board[i][j] > MAX) MAX = fisrt_board[i][j];
			}
		}
	}
	dfs(fisrt_board, 0);
	printf("%d", MAX);
	return 0;
}