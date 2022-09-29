//#include <iostream>
//#include <queue>
//#define INF 1e10;
//
//int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };
//
//struct E {
//	int V;
//	int i;
//	int j;
//	E(int a, int b, int c) {
//		V = a;
//		i = b;
//		j = c;
//	}
//	bool operator<(const E &b)const {
//		return V > b.V;
//	}
//};
//
//int main() {
//	std::priority_queue <E> PQ;
//	PQ.emplace(1,2,3);
//	PQ.emplace(0, 0, 0);
//	PQ.emplace(6, 4, 2);
//	PQ.emplace(4, 3, 3);
//	PQ.emplace(9, 3, 2);
//	while (!PQ.empty()) {
//		printf("%d %d %d\n", PQ.top().V, PQ.top().i, PQ.top().j);
//		PQ.pop();
//	}
//
//}