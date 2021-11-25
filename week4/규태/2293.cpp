#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, K;
    int coin[101] = { 0, };
    int dp[10001] = { 1, 0, };

    cin >> N >> K;

    for (int i = 0; i < N; i++) {
        cin >> coin[i];
        for (int k = coin[i]; k <= K; k++)
            dp[k] = dp[k] + dp[k - coin[i]];
    }

    cout << dp[K] << '\n';

    return 0;
}
