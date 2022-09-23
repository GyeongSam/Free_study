#include <iostream>
#include <vector>
#include <set>

int di[5] = {0,-1,1,0,0}, dj[5] = {0,0,0,-1,1};

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N, M, K,i,j,A,D;
		std::vector<std::pair<int, int>> cell[100][100];
		std::set<std::pair<int, int>> A_list;
		std::set<std::pair<int, int>> B_list;

		scanf("%d %d %d", &N, &M, &K);

		while (K--) {
			scanf("%d %d %d %d", &i, &j, &A, &D);
			A_list.insert({ i, j });
			cell[i][j].emplace_back(A, D);
		}


		while(M--){

			for (std::set<std::pair<int, int>>::iterator iter = A_list.begin(); iter != A_list.end();++iter){
				i = (*iter).first; j = (*iter).second;
				int d = cell[i][j][0].second;
				int I = i + di[d], J = j + dj[d];
				cell[I][J].emplace_back(cell[i][j][0].first, d);
				cell[i][j].erase(cell[i][j].begin());
				B_list.insert({ I, J });
			}
			A_list.clear();

			for (std::set<std::pair<int, int>>::iterator iter = B_list.begin(); iter != B_list.end(); ++iter) {
				i = (*iter).first; j = (*iter).second;
				int sum = cell[i][j][0].first,max=sum, d=cell[i][j][0].second;
				if (i == 0 || i == N - 1 || j == 0 || j == N - 1) {
					sum /= 2;
					if (d == 1) d = 2;
					else if(d == 2) d = 1;
					else if(d == 3) d = 4;
					else d = 3;
				}
				
				if (cell[i][j].size() > 1) {
					for (int n = 1; n < cell[i][j].size(); ++n) {
						sum += cell[i][j][n].first;
						if (cell[i][j][n].first > max) {
							max = cell[i][j][n].first;
							d = cell[i][j][n].second;
						}
					}
				}
				cell[i][j].clear();
				cell[i][j].emplace_back(sum, d);
				A_list = B_list;
			}
			B_list.clear();

		}
		int ans=0;
		for (std::set<std::pair<int, int>>::iterator iter = A_list.begin(); iter != A_list.end(); ++iter) {
			i = (*iter).first; j = (*iter).second;
			ans += cell[i][j][0].first;
		}
		printf("#%d %d\n", t, ans);
	}
}

//for (int y = 0; y < N; ++y) {
//	for (int x = 0; x < N; ++x) {
//		if (cell[y][x].empty()) printf("(0,0) ");
//		else printf("(%d %d) ", cell[y][x][0].first, cell[y][x][0].second);
//	}
//	printf("\n");
//}
//printf("\n");