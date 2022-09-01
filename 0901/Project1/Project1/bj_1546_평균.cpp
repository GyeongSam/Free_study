#include <iostream>
#include <vector>

int main() {
	int n,sum=0,M=0;
	std::cin >> n;
	std::vector<int> L;
	for (int i = 0; i < n; ++i) {
		int l;
		std::cin >> l;
		sum += l;
		if (l > M)M = l;
		L.push_back(l);
	}
	float avg = (float) sum*100 /(n*M);
	std::cout << avg << '\n';
	return 0;
}