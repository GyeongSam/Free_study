#include <iostream>
#include <vector>

int main() {
	int T;
	std::cin >> T;
	for (int t=1; t <= T;t++) {
		int N, CAN=1;
		std::cin >> N;
		std::vector<std::vector<int>> s(1, std::vector<int> {});
		std::vector<int> sub;

		for (int i = 0; i < N; i++) {
			std::vector<std::vector<int>> SUB;
			for (int q = 0; q < s.size(); q++) {
				for (int j = 0; j < N; j++) {

					sub = s[q];

					int t = j, b = j, can = 1;

					if (sub.empty() != 1) {
						for (int k = sub.size() - 1; k >= 0; k--) {
							if (sub[k] == j or ++t == sub[k] or --b == sub[k]) {
								can = 0;
								break;
							}
						}
					}
					if (can) {
						sub.push_back(j);
						SUB.push_back(sub);
					}
				}
				}
				if (SUB.empty()) { CAN = 0; break; }
				else s = SUB;

			if (CAN==0) break;
		}

	std::cout << "#"<<t<<" "<< (CAN?s.size():0) << "\n";}
	
}
	