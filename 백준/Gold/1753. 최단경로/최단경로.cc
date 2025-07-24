#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

#define MAX 20001
#define INF 1e9

int V, E, K;
vector<pair<int, int>> adj[MAX];
int dist[MAX];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> V >> E;
    cin >> K;

    for (int i = 0; i < E; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({ v,w });
    }

    for (size_t i = 1; i <= V; i++)
    {
        dist[i] = INF;
    }
    dist[K] = 0;

    priority_queue < pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({ 0,K });

    while (!pq.empty()) {
        int d = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (dist[now] < d)
            continue;

        for (auto& edge : adj[now])
        {
            int next = edge.first;
            int cost = edge.second;
            if (dist[next] > dist[now] + cost) {
                dist[next] = dist[now] + cost;
                pq.push({ dist[next] ,next });
            }
        }
    }

    for (int i = 1; i <= V; i++)
    {
        if (dist[i] == INF) {
            cout << "INF\n";
        }
        else {
            cout << dist[i] << "\n";
        }
    }
    
    return 0;
}
