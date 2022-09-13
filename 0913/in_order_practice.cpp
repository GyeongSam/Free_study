#include <iostream>

int N, trash;
char tree[101], sub[10];

void in_order(int n) {
    if (n > 0 && n <= N) {
        in_order(2 * n);
        std::cout << tree[n];
        in_order(2 * n + 1);
    }
}

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    for (int T = 1; T <= 10; T++) {
        std::cin >> N;

        for (int i = 1; i <= N; i++) {
            std::cin >> trash;
            std::cin.ignore();
            std::cin.getline(sub, 10);
            tree[i] = sub[0];
        }
        std::cout << "#" << T << " ";
        in_order(1);
        std::cout << "\n";
    }

}