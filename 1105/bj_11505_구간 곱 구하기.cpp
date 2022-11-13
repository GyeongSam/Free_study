//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <vector>
//#define BN 1000000007
//
//using namespace std;
//
//struct segmenttree {
//	vector <int> tree;
//	vector <int> zerotree;
//	int r, l;
//	int s, e;
//	void setting(vector <int> nums) {
//		l = 0;
//		r = nums.size() - 1;
//		int n = 1;
//		while (n * n++ < r);
//		tree.resize(n * n * 2, 1);
//		zerotree.resize(n * n * 2, 1);
//		make(nums, 1, l, r);
//		makezerotree(nums, 1, l, r);
//	}
//	int make(vector <int>nums, int idx, int l, int r) {
//		if (l >= r) {
//			if (!nums[l]) {
//				tree[idx] = 1;
//			}
//			else tree[idx] = nums[l];
//			return tree[idx];
//		}
//		else {
//			int m = (l + r) / 2;
//			tree[idx] = (make(nums, 2 * idx, l, m) % BN) * (make(nums, 2 * idx + 1, m + 1, r) % BN) % BN;
//			return tree[idx];
//		}
//	}
//	int makezerotree(vector <int>nums, int idx, int l, int r) {
//		if (l >= r) {
//			zerotree[idx] = nums[l];
//			return zerotree[idx];
//		}
//		else {
//			int m = (l + r) / 2;
//			zerotree[idx] = (makezerotree(nums, 2 * idx, l, m) % BN) * (makezerotree(nums, 2 * idx + 1, m + 1, r) % BN) % BN;
//			return zerotree[idx];
//		}
//	}
//
//
//	void edit(int edit_index, int before_num, int edit_num) {
//		int edit_r = r;
//		int edit_l = l;
//		int idx = 1;
//		if (!before_num) {
//			before_num = 1;
//
//			while (edit_l < edit_r) {
//				tree[idx] = (tree[idx] * edit_num / before_num) % BN;
//				zerotree[idx] = tree[idx];
//				int m = (edit_r + edit_l) / 2;
//				if (edit_index > m) {
//					idx = idx * 2 + 1;
//					edit_l = m + 1;
//				}
//				else {
//					idx = idx * 2;
//					edit_r = m;
//				}
//			}
//			tree[idx] = (tree[idx] * edit_num / before_num) % BN;
//			zerotree[idx] = tree[idx];
//		}
//
//		else if (!edit_num) {
//			edit_num = 1;
//			while (edit_l < edit_r) {
//				tree[idx] = (tree[idx] * edit_num / before_num) % BN;
//				zerotree[idx] = 0;
//				int m = (edit_r + edit_l) / 2;
//				if (edit_index > m) {
//					idx = idx * 2 + 1;
//					edit_l = m + 1;
//				}
//				else {
//					idx = idx * 2;
//					edit_r = m;
//				}
//			}
//			tree[idx] = (tree[idx] * edit_num / before_num) % BN;
//			zerotree[idx] = 0;
//		}
//
//		else {
//			while (edit_l < edit_r) {
//				tree[idx] = (tree[idx] * edit_num / before_num) % BN;
//				zerotree[idx] = tree[idx];
//				int m = (edit_r + edit_l) / 2;
//				if (edit_index > m) {
//					idx = idx * 2 + 1;
//					edit_l = m + 1;
//				}
//				else {
//					idx = idx * 2;
//					edit_r = m;
//				}
//			}
//			tree[idx] = (tree[idx] * edit_num / before_num) % BN;
//			zerotree[idx] = tree[idx];
//		}
//		
//	}
//	int temp(int ss,int ee) {
//		s = ss;
//		e = ee;
//		return product(1, l, r);
//	}
//	int product(int idx, int l, int r) {
//		if (s <= l && r <= e) return tree[idx];
//
//		else if (e<l || s>r) return 1;
//		else {
//			int m = (l + r) / 2;
//			return (product(idx * 2, l, m) % BN) * (product(idx * 2 + 1, m + 1, r) % BN) % BN;
//
//		}
//	}
//	int zerotemp(int ss, int ee) {
//		s = ss;
//		e = ee;
//		return zeroproduct(1, l, r);
//	}
//	int zeroproduct(int idx, int l, int r) {
//		if (s <= l && r <= e) return zerotree[idx];
//
//		else if (e<l || s>r) return 1;
//		else {
//			int m = (l + r) / 2;
//			return (zeroproduct(idx * 2, l, m) % BN) * (zeroproduct(idx * 2 + 1, m + 1, r) % BN) % BN;
//		}
//	}
//
//
//};
//
//
//int main() {
//	segmenttree A;
//	vector <int> ip;
//	int N, M, K;
//	scanf("%d %d %d", &N, &M, &K);
//
//	ip.resize(N, 0);
//	for (int i = 0; i < N; ++i) scanf("%d", &ip[i]);
//	A.setting(ip);
//
//	int a, b, c;
//	for (int i = 0; i < N + M; ++i) {
//		scanf("%d %d %d", &a, &b, &c);
//		if (a == 1) {
//			A.edit(b - 1, ip[b - 1], c);
//			ip[b - 1] = c;
//		}
//		else {
//			int ZX = A.zerotemp(b - 1, c - 1);
//			if (ZX) printf("%d\n", A.temp(b - 1, c - 1));
//			else printf("0\n");
//		}
//	}
//
//}