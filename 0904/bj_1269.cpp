#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	int N, M;
	std::cin >> N >> M;
	int *L = (int*)malloc(N * sizeof(int));
	for (int i = 0; i < N; i++) {
		std::cin >> *(L + i);
	}
	int sub,cnt=0;
	for (int i = 0; i < M; i++) {
		std::cin >> sub;
		for (int j = 0; j < N; j++) {
			if (L[j] == sub) {
				cnt+=2;
				L[j] = 0;
				break;
			}
		}
	}
	std::cout<< N+M-cnt<<"\n";

	/*for (int i = 0; i < N; i++) {
		std::cout << *(L + i);
	}*/

}