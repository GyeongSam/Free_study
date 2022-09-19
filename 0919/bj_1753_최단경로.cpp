#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;


int V, E, S,st,ed,va,f1,q;
vector<int> G[20001];
vector<int> value[20001];
queue<int> Q;
int ans[20001];

int main() {
	scanf("%d %d",&V, &E);
	scanf("%d", &S);
	Q.push(S);
	fill(ans, ans + V+1, 1e7);
	ans[S] = 0;
	//for (int i = 1; i <= V; ++i) {
	//	printf("%d ", ans[i]);
	//}
	//printf("\n");

	for (int v = 0; v < E; ++v) {
		scanf("%d %d %d", &st, &ed, &va);
		f1 = 0;
		if (G[st].empty()) {
			G[st].push_back(ed);
			value[st].push_back(va);
		}
		else {
			for (int i = 0; i < G[st].size(); ++i) {
				if (G[st][i] == ed) {
					value[st][i] = min(value[st][i], va);
					f1 = 1;
					break;
				}
			}
			if (!f1) {
				G[st].push_back(ed);
				value[st].push_back(va);
			}
		}
	}
	
	//for (int i = 1; i <= V; ++i) {
	//	printf("%d :", i);
	//	for (int j = 0; j < G[i].size(); ++j) {
	//		printf("%d ", G[i][j]);
	//	}
	//	printf("\n");
	//}
	//printf("\n");

	//for (int i = 1; i <= V; ++i) {
	//	printf("%d :", i);
	//	for (int j = 0; j < value[i].size(); ++j) {
	//		printf("%d ", value[i][j]);
	//	}
	//	printf("\n");
	//}
	//printf("\n");




	while (!Q.empty()) {
		q = Q.front();
		Q.pop();
		for (int i = 0; i < G[q].size(); ++i) {
			if (ans[G[q][i]] > ans[q] + value[q][i]) {
				ans[G[q][i]] = ans[q] + value[q][i];
				Q.push(G[q][i]);
			}
		}
		
	}
	for (int i = 1; i <= V; ++i) {
		if(ans[i]!=1e7) printf("%d\n", ans[i]);
		else printf("INF\n");
	}


}