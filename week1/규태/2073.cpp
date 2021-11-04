#include <iostream>

using namespace std;

int dp[100001] = { NULL, };
int past[100001] = { NULL, };

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int D, P;
    pair<int, int> pipe[352];

    cin >> D >> P;
    for (int i = 1; i <= P; i++)
        cin >> pipe[i].first >> pipe[i].second;

    for (int i = 1; i <= P; i++) {
        for (int k = 1; k <= D; k++) {
            if (k == pipe[i].first)
                dp[k] = max(dp[k], pipe[i].first);
            else if (k > pipe[i].first) {
                int tmp = min(past[k - pipe[i].first], pipe[i].second);
                dp[k] = max(dp[k], tmp);
            }
        }

        for (int k = 1; k <= D; k++)
            past[k] = dp[k];
    }

    cout << dp[D] << '\n';

    return 0;
}
