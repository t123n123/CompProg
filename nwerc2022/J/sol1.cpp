#include <bits/stdc++.h>

using namespace std;

vector<pair<pair<int, int>, int>> segments = {};

int main() {
    // Time Complex: N^2
    int n;
    scanf("%d", &n);

    vector<int> result(n + 3);
    for (int i = 1; i <= n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);

        // y is now end of segment, not length
        y = x + y;

        // ((start, end), index) - index used to keep order after sorting
        segments.push_back({{x, y}, i});
    }

    // sort segments by length -> lower first
    sort(segments.begin(), segments.end(),
         [](const pair<pair<int, int>, int> a,
            const pair<pair<int, int>, int> b) {
             return (a.first.second - a.first.first) <=
                    (b.first.second - b.first.first);
         });

    for (int i = n - 1; i >= 0; i--) {
        int value = 0;
        for (int j = i + 1; j < n; j++) {
            if (segments[j].first.first <= segments[i].first.first &&
                segments[j].first.second >= segments[i].first.second) {
                value = max(result[segments[j].second] + 1, value);
            }
        }
        result[segments[i].second] = value;
    }

    // output
    for (int i = 1; i <= n; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
}
