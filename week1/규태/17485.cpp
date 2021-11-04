#include <iostream>
#include <algorithm>

using namespace std;

int oil[1001][1001] = { 0, };
int memo[1001][1001][3] = { 0, };

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, M;
    int result = 100001;

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int k = 0; k < M; k++)
            cin >> oil[i][k];
    
    for (int k = 0; k < M; k++) {
        memo[0][k][0] = oil[0][k];
        memo[0][k][1] = oil[0][k];
        memo[0][k][2] = oil[0][k];
    }

    for (int i = 1; i < N; i++) {
        for (int k = 0; k < M; k++) {
            if (k == 0) {
                memo[i][k][0] = 100001;
                memo[i][k][1] = memo[i - 1][k][2] + oil[i][k];
                memo[i][k][2] = min(memo[i - 1][k+1][0], memo[i - 1][k+1][1]) + oil[i][k];
            }
            else if (k == M - 1) {
                memo[i][k][0] = min(memo[i - 1][k-1][1], memo[i - 1][k-1][2]) + oil[i][k];
                memo[i][k][1] = memo[i - 1][k][0] + oil[i][k];
                memo[i][k][2] = 100001;
            }
            else {
                memo[i][k][0] = min(memo[i - 1][k-1][1], memo[i - 1][k-1][2]) + oil[i][k];
                memo[i][k][1] = min(memo[i - 1][k][0], memo[i - 1][k][2]) + oil[i][k];
                memo[i][k][2] = min(memo[i - 1][k+1][0], memo[i - 1][k+1][1]) + oil[i][k];
            }
        }
    }
    
    for (int k = 0; k < M; k++)
        for (int h = 0; h < 3; h++)
            if (result > memo[N - 1][k][h])
                result = memo[N - 1][k][h];

    cout << result;

    return 0;
}
