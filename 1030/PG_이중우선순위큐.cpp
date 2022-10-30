#include <string>
#include <vector>

using namespace std;


void swap(int *a,int*b) {
    int temp = *b;
    *b = *a;
    *a = temp;
}

void maxheappush(vector<int>& maxheap, vector<int>& minheap, vector<int>& mtom, int ip) {
    int idx = maxheap.size();
    maxheap.push_back(ip);
    while (idx > 1 && maxheap[idx / 2] < maxheap[idx]) {
        swap(maxheap[idx / 2], maxheap[idx]);
        idx /= 2;
    }
    int idx2 = minheap.size();
    minheap.push_back(ip);
    while (idx2 > 1 && minheap[idx2 / 2] > minheap[idx2]) {
        swap(minheap[idx2 / 2], minheap[idx2]);
        idx2 /= 2;
    }


}
void maxheappop(vector<int>& maxheap, vector<int>& maxtomin) {
    int last_idx = maxheap.size() - 1;
    swap(maxheap[1], maxheap[last_idx--]);
    maxheap.pop_back();
    int idx = 1;
    while (1) {
        if ((last_idx >= (2 * idx + 1) && maxheap[2 * idx] >= maxheap[2 * idx + 1] && maxheap[idx] < maxheap[2 * idx]) || (last_idx == (2 * idx) && maxheap[2 * idx] > maxheap[idx])) {
            swap(maxheap[idx], maxheap[2 * idx]);
            idx *= 2;
        }
        else if (last_idx >= (2 * idx + 1) && maxheap[2 * idx + 1] > maxheap[2 * idx] && maxheap[idx] < maxheap[2 * idx + 1]) {
            swap(maxheap[idx], maxheap[2 * idx + 1]);
            idx = 2 * idx + 1;
        }
        else break;
    }
}
void minheappush(vector<int>& minheap, vector<int>& mintomax, int ip) {
    int idx = minheap.size();
    minheap.push_back(ip);
    while (idx > 1 && minheap[idx / 2] > minheap[idx]) {
        swap(minheap[idx / 2], minheap[idx]);
        idx /= 2;
    }
}
void minheappop(vector<int>& minheap, vector<int>& mintomax) {
    int last_idx = minheap.size() - 1;
    swap(minheap[1], minheap[last_idx--]);
    minheap.pop_back();
    int idx = 1;
    while (1) {
        if ((last_idx >= (2 * idx + 1) && minheap[2 * idx] <= minheap[2 * idx + 1] && minheap[idx] > minheap[2 * idx]) || (last_idx == (2 * idx) && minheap[2 * idx] < minheap[idx])) {
            swap(minheap[idx], minheap[2 * idx]);
            idx *= 2;
        }
        else if (last_idx >= (2 * idx + 1) && minheap[2 * idx + 1] < minheap[2 * idx] && minheap[idx] > minheap[2 * idx + 1]) {
            swap(minheap[idx], minheap[2 * idx + 1]);
            idx = 2 * idx + 1;
        }
        else break;
    }
}

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    vector<int> maxheap(1, 0);
    vector<int> minheap(1, 0);
    vector<int> mtom(1, 0);




    for (int a = 0; a < operations.size(); ++a) {
        if (operations[a] == "D 1" && maxheap.size()>1){
            
        }

        else if (operations[a] == "D -1" && minheap.size() > 1) {
            
        }

        else {
            string num(operations[a], 2, operations[a].length() - 2);
            int n = stoi(num);
            maxheappush(maxheap, n);
            minheappush(minheap, n);
        }


    }
    if (maxheap.size() > 1) answer.push_back(maxheap[1]);
    else answer.push_back(0);
    if (minheap.size() > 1) answer.push_back(minheap[1]);
    else answer.push_back(0);

    return answer;
}