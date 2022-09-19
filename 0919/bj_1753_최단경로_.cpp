#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int V, E, S, st, ed, va, f1, q;
int edge[20001][20001] = { 0, };
queue<int> Q;
int ans[20001];

int main() {
	scanf("%d %d", &V, &E);
	scanf("%d", &S);
	Q.push(S);
	fill(ans, ans + V + 1, 1e7);
	ans[S] = 0;

	for (int v = 0; v < E; ++v) {
		scanf("%d %d %d", &st, &ed, &va);
		if (edge[st][ed]) {
			if (edge[st][ed] > va) edge[st][ed] = va;
		}
		else edge[st][ed] = va;
	}

	while (!Q.empty()) {
		q = Q.front();
		Q.pop();
		for (int i = 1; i <= V; ++i) {
			if (edge[q][i]) {
				if (edge[q][i]+ans[q]<ans[i])
					ans[i] = ans[q] + edge[q][i];
					Q.push(i);
			}
		}

	}
	for (int i = 1; i <= V; ++i) {
		if (ans[i] != 1e7) printf("%d\n", ans[i]);
		else printf("INF\n");
	}
}