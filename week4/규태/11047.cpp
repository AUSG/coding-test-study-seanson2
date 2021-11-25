#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, K, cnt = 0;;
    int A[11] = { 0, };

    cin >> N >> K;
    for (int i = 0; i < N; i++)
        cin >> A[i];

    for (int i = N - 1; i >= 0; i--) {
        while (K - A[i] >= 0) {
            K -= A[i];
            cnt++;
        }
    }

    cout << cnt << '\n';

    return 0;
}
