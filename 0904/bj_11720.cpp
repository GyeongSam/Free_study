#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);
	int N,sum=0;
	char Nums[101];
	std::cin >> N;
	std::cin.ignore();
	std::cin.getline(Nums, 101);
	for (int i = 0; i < N; i++) {
		sum += Nums[i] - '0';
	}
	std::cout << sum << "\n";
}