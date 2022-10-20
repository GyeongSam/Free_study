#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

int N;

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void push(int *heap,int idx, int num) {
	heap[idx] = num;
	while (idx >= 2 && heap[idx / 2] < heap[idx]) {
		swap(&heap[idx / 2], &heap[idx]);
		idx /= 2;
	}
}

void replace(int* heap,int idx, int num) {
	heap[1] = num;
	int a = 1;
	while (1) {
		if ((2 * a + 1 <= idx && heap[a]<heap[2 * a] && heap[2 * a]>=heap[2 * a + 1]) || (2 * a == idx && heap[a] < heap[2 * a])) {
			swap(&heap[2 * a], &heap[a]);
			a *= 2;
		}
		else if ((2 * a + 1 <= idx && heap[a] < heap[2 * a + 1] && heap[2 * a] < heap[2 * a + 1])) {
			swap(&heap[2 * a + 1], &heap[a]);
			a = 2 * a + 1;
		}
		else break;
	}
}

int main() {
	int max_heap[50005];
	int iM = 0;
	int min_heap[50005];
	int im = 0;
	int center;
	scanf("%d", &N);
	scanf("%d", &center);
	printf("%d\n", center);
	int sub;
	for (int n = 1; n < N; ++n) {
		scanf("%d", &sub);

		if (n % 2) {
			if (sub > center) {
				push(min_heap, ++im, -sub);
			}
			else if (iM==0 || sub > max_heap[1]) {
				push(min_heap, ++im, -center);
				center = sub;
			}
			else {
				push(min_heap, ++im, -center);
				center = max_heap[1];
				replace(max_heap, iM, sub);
			}
		}

		else {
			if (sub < center) {
				push(max_heap, ++iM, sub);
			}
			else if(im==0 || sub < -min_heap[1]) {
				push(max_heap, ++iM, center);
				center = sub;
			}
			else {
				push(max_heap, ++iM, center);
				center = -min_heap[1];
				replace(min_heap, im, -sub);
			}
		}
		printf("%d\n", center);
	}
}