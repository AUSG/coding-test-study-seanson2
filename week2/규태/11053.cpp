#include <iostream>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, result = 0;
    int num[1001] = { 0, };
    int cnt[1001] = { 0, };

    cin >> N;
    for (int i = 0; i < N; i++) {
        int count = 0;

        cin >> num[i];
        for (int k = 0; k < i; k++) 
            if (num[i] > num[k])
                if (count < cnt[k])
                    count = cnt[k];
        
        cnt[i] = count + 1;
        if (result < cnt[i])
            result = cnt[i];
    }

    cout << result << '\n';

    return 0;
}
