#include <iostream>

int main() {
	char sugyeong[11]={ 0, };
	
	for (int i = 0; i < 10; ++i) printf("%c ", sugyeong[i]);
	printf("\n");
	printf("%d ", sugyeong[0] == 's');
	printf("%d ", sugyeong[1] == 'u');
	printf("%d ", sugyeong[2] == 'g');
	printf("%d ", sugyeong[3] == 'y');
	printf("%d ", sugyeong[4] == 'e');
}