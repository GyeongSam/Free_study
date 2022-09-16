#include <iostream>

void star(int c,int I) {
	if (c == 0) {
		if (I == 4) std::cout << " ";
		std::cout << "*";
	}
	for (int i = 0; i < 9; i++) {
		star(c - 1, i);
		if (i / 3 == 2) std::cout << "\n";
	}

}

int main() {
	star(1,0);
}