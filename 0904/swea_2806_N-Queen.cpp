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

						/*std::cout << "이번 sub " << "\n";
						for (int z = 0; z < sub.size(); z++) std::cout << sub[z] << " ";
						std::cout << "\n";*/

						SUB.push_back(sub);


					}

				}
			
				}
				//std::cout << "empty" << SUB.empty() << "\n";
				if (SUB.empty()) { CAN = 0; break; }
				else s = SUB;

				//std::cout << "이번 s " << "\n";
				//for (int z = 0; z < s.size(); z++) {
				//	for (int x = 0; x < s[z].size(); x++) {
				//		std::cout << s[z][x] << " ";
				//	}
				//	std::cout << "\n";
			if (CAN==0) break;
		}

	std::cout << "#"<<t<<" "<< (CAN?s.size():0) << "\n";}
	
}
	