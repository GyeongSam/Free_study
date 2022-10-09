#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char a[101];
	scanf("%s", &a);
	for (int i = 0; a[i] != '\0'; ++i) {
		if (a[i] > 95) printf("%c", a[i] - 32);
		else printf("%c", a[i] + 32);
	}
}