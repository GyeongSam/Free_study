#include <iostream>

struct stone {
	int Y;
	int X;
	int C;
};

int T,N,M,X,Y,S,B,W;
int board[10][10];
int dx[8] = {1,0,-1,0,-1,1,1,-1};
int dy[8] = {0,1,0,-1,1,-1,1,-1};
int swap[10];
stone sub, D;


void GO(stone A) {
	int B = 3 - A.C;
	board[A.Y][A.X] = A.C;
	for (int d = 0; d < 8; ++d) {
		D.X = A.X + dx[d];
		D.Y = A.Y + dy[d];
		while (board[D.Y][D.X]==B) {
			D.X += dx[d];
			D.Y += dy[d];
		}
		if (board[D.Y][D.X] == A.C) {
			D.X -= dx[d];
			D.Y -= dy[d];
			while (board[D.Y][D.X] == B) {
				board[D.Y][D.X] = A.C;
				D.X -= dx[d];
				D.Y -= dy[d];
			}
		}
	}
}


int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		B = 0;
		W = 0;
		scanf("%d %d", &N, &M);
		int n = N / 2;
		for (int y = 0; y <= N+1; ++y) {
			for (int x = 0; x <= N+1; ++x) {
				if ((x == n && y == n) or (x == n + 1 && y == n + 1)) board[y][x] = 2;
				else if ((x == n && y == n+1) or (x == n +1 && y == n)) board[y][x] = 1;
				else board[y][x] = 0;
			}
		}

		
		while (M--) {
			scanf("%d %d %d", &sub.X, &sub.Y, &sub.C);
			GO(sub);
			/*for (int y = 1; y <= N; ++y) {
				for (int x = 1; x <= N; ++x) {
					printf("%d ", board[y][x]);
				}
				printf("\n");
			}
			printf("\n");*/
		}
		for (int y = 1; y <= N; ++y) {
			for (int x = 1; x <= N; ++x) {
				if (board[y][x] == 2) ++W;
				else if (board[y][x] == 1) ++B;
			}
		}
		printf("#%d %d %d\n", t, B, W);
	}
}