#include <iostream>
#include <set>

int main() {
	int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int data[4][4];
		std::set<int> ans;
		std::set<int> now[4][4];
		std::set<int> next[4][4];
		int sub;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%d", &data[i][j]);
				now[i][j].insert(data[i][j]);
			}
		}
		int a = 6;
		while (a--) {
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					for (int d = 0; d < 4; ++d) {
						int I = i + di[d];
						int J = j + dj[d];
						if (I < 0 || I>3 || J < 0 || J>3) continue;
						for (std::set<int>::iterator iter = now[I][J].begin(); iter != now[I][J].end(); iter++) {
							if (!a) next[0][0].insert((*iter) * 10 + data[i][j]);
							else next[i][j].insert((*iter) * 10 + data[i][j]);
						}
					}
				}
			}
			if (!a) break;
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					now[i][j] = next[i][j];
					next[i][j].clear();
				}
			}
		}
		printf("#%d %d\n", t, next[0][0].size());

	}
}


/*for (std::set<int>::iterator iter = next[0][0].begin(); iter != next[0][0].end(); iter++) {
			printf("%d,", *iter);}*/

			/*for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					printf("(");
					for (std::set<int>::iterator iter = now[i][j].begin(); iter != now[i][j].end(); iter++) {
						printf("%d,", *iter);
					}
					printf(") ");
				}
				printf("\n");
			}*/