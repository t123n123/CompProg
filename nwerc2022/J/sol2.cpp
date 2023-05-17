#include <bits/stdc++.h> 

using namespace std;

struct Segment{
    int x;
    int y;
    int len;
    int index;
};
struct Endpoint{
    int x;
    bool is_start;
    int index;
    int len;
};

vector<Segment> segments;
vector<int> result;
vector<Endpoint> endpoints;
vector<pair<int,int>> endpoint_indicies;
int main() {
    int n;
    scanf("%d", &n);
    segments.resize(n);
    result.resize(n);
    for (int i = 0; i < n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        segments[i].x = x;
        segments[i].y = x + y;
        segments[i].len = y;
        segments[i].index = i;

        endpoints.push_back(Endpoint {.x = x, .is_start = true, .index = i, .len = y});
        endpoints.push_back(Endpoint {.x = x+y, .is_start = false, .index = i, .len = y});
    }
    endpoint_indicies.resize(n);

    // Sort endpoints by .x
    // If same .x and both starts -> bigger comes first 
    // If both ends -> bigger last
    sort(endpoints.begin(), endpoints.end(), 
        [](const Endpoint a, const Endpoint b) {
            if(a.x != b.x) {
                return a.x < b.x;
            }
            if(a.is_start != b.is_start) {
                return a.is_start;
            }
            if(a.is_start) 
                return a.len > b.len;
            else
                return a.len < b.len;
        }
    );
    
    // Save indicies of endpoints of each segment 
    for (int i = 0; i < n*2; i++) {
        Endpoint endpoint = endpoints[i];
        // printf("%d %d %c \n",endpoint.index ,endpoint.x ,(endpoint.is_start ? 'S' : 'E'));
        if(endpoint.is_start) {
            endpoint_indicies[endpoint.index].first = i;
        } else {
            endpoint_indicies[endpoint.index].second = i;
        }
    }
    
    vector<int> max_result(2*n);
    
    // This is O(n)
    for (int i = 0; i < n*2; i++) {
        Endpoint endpoint = endpoints[i];
        if(endpoint.is_start) {
            // get max val at position of the second endpoint 
            int result_i = max_result[endpoint_indicies[endpoint.index].second];
            // shift local result by 1 for easy computation
            result_i += 1;
            // final result = local result - 1
            result[endpoint.index] = result_i - 1; 

            // any segment begining after this one, with right endpoint in this segment 
            // could inherit this result + 1
           
            // This is O(n) so total O(n^2) 
            // possible optimization Lazy Propag Segment Tree
            for(int j = i; j < endpoint_indicies[endpoint.index].second; j++) {
                max_result[j] = max(max_result[j], result_i);
            }
        }
    }

    for(int i = 0; i < n; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

}
