#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int level[100001] = { 0, 1, 0,};
int parent[100001] = { 0, };
vector<int> graph[100001];

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    queue<int> que;

    int N, lev = 1;

    cin >> N;

    for (int i = 1; i < N; i++) {
        int num1, num2;

        cin >> num1 >> num2;
        graph[num1].push_back(num2);
        graph[num2].push_back(num1);
    }

    que.push(1);
    while (1)
    {
        int cnt = que.size();

        lev++;
        while (cnt--) {
            for (int i = 0; i < graph[que.front()].size(); i++) {
                if (level[graph[que.front()][i]] == 0) {
                    level[graph[que.front()][i]] = lev;
                    parent[graph[que.front()][i]] = que.front();
                    que.push(graph[que.front()][i]);
                }
            }
            que.pop();
        }
        if (que.size() == 0)
            break;
    }

    for (int i = 2; i <= N; i++)
        cout << parent[i] << '\n';
    

    return 0;
}
