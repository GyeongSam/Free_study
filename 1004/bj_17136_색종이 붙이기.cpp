#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

int min=26;
int feild[10][10] = { 0, };
long long cnt[6];

void dfs() {
	int notyet=0,i,j;

	for (i = 0; i < 10; ++i) {
		for (j = 0; j < 10; ++j) {
			if (feild[i][j]) { notyet = 1; break; }
		}
		if (notyet) break;
	}

	if (notyet) {
		for (int l = 5; l > 0; --l) {
			if (cnt[l]) {
				int check = 0;
				for (int di = 0; di < l; ++di) {
					for (int dj = 0; dj < l; ++dj) {
						if (i+di>9 || j+dj>9 || !feild[i + di][j + dj]) {
							check = 1; break;
						}
					}
				}
				if (!check) {
					for (int di = 0; di < l; ++di) {
						for (int dj = 0; dj < l; ++dj) {
							feild[i + di][j + dj] = 0;
						}
					}
					--cnt[l];
					dfs();
					++cnt[l];
					for (int di = 0; di < l; ++di) {
						for (int dj = 0; dj < l; ++dj) {
							feild[i + di][j + dj] = 1;
						}
					}
				}
			}
		}
	}
	else {
		if (min > (25 - cnt[1] - cnt[2] - cnt[3] - cnt[4] - cnt[5])) {
			min = (25 - cnt[1] - cnt[2] - cnt[3] - cnt[4] - cnt[5]);
		}
	}

}

int main() {
	for (int i = 0; i < 6; ++i) cnt[i] = 5;
	for (int i = 0; i < 10; ++i) {
		for (int j = 0; j < 10; ++j) {
			scanf("%d", &feild[i][j]);
		}
	}
	dfs();
	if (min == 26) {
		printf("%d", -1);
	}
	else printf("%d", min);
}