#include <iostream>


int swap(int *a, int *b) {
	int temp = *b;
	*b = *a;
	*a = temp;
	return 0;
}







int main() {
	int t,T=1;
	std::cin >> t;
	for (; T <= t; T++) {
		int N, S, i = 0;
		int Arr_N[6];
		std::cin >> N >> S;
		
		while (N != 0) {
			Arr_N[i++] = N % 10;
			N /= 10;
		}
		std::cout << "\n";
		for (int j = 0; j < i; j++) std::cout << Arr_N[j] << " ";
	}
}