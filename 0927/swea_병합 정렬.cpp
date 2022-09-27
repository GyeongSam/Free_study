#include <iostream>

int num_list[1000000];
int sorted_list[1000000];
int cnt;

void devide(int,int);
void merge(int,int);

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N;
		cnt = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)sorted_list[i] = 0;
		for (int n = 0; n < N; ++n) {
			scanf("%d", &num_list[n]);
		}
		devide(0, N - 1);
		printf("#%d %d %d\n",t,sorted_list[N/2], cnt);
	}
}

void devide(int start,int end) {
	if (start < end) {
		int mid = (start + end+1) / 2 - 1;
		devide(start, mid);
		devide(mid + 1, end);
		merge(start, end);
	}
}
void merge(int start,int end) {
	int mid = (start + end+1) / 2 -1;
	int l = start, r = mid+1;
	if (num_list[mid] > num_list[end])++cnt;

	for (int i = start; i <= end; ++i) {
		if (l <= mid && (r > end || num_list[l] < num_list[r])) {
			sorted_list[i] = num_list[l++];
		}
		else if (r <= end && (l > mid || num_list[r] <= num_list[l])) {
			sorted_list[i] = num_list[r++];
		}
	}
	for (int i = start; i <= end; ++i) num_list[i]=sorted_list[i];
}