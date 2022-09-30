#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> arr;

int main(void) {
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }

    sort(arr.begin(), arr.end());

    int result = 0;
    int count = 0;
    for (int i = 0; i < n; i++) {
        count += 1;
        if (count >= arr[i]) {
            result += 1;
            count = 0;
        }
    }

    cout << result << '\n';
}
