#include <iostream>

using namespace std;

bool arr[129][129];
pair<int, int> result = { 0, 0 };

void DFS(int N, int x0, int y0, int x1, int y1) {

    if (N == 1) {
        if (arr[y0][x0] == 1) {
            result.first++;
            return;
        }
        else {
            result.second++;
            return;
        }
    }

    bool check = false;
    for (int i = y0; i <= y1; i++) {
        for (int k = x0; k <= x1; k++) {
            if (arr[i][k] != arr[y0][x0]) {
                check = true;
                break;
            }
        }
        if (check == true) {
            DFS(N / 2, x0, y0, x0 + (N/2-1), y0 + (N / 2 - 1));  // 0033
            DFS(N / 2, x1 - (N / 2 - 1), y1 - (N / 2 - 1), x1, y1);  // 4477
            DFS(N / 2, x0, y1 - (N / 2 - 1), x0 + (N / 2 - 1), y1); //4073
            DFS(N / 2, x1 - (N / 2 - 1), y0, x1, y0 + (N / 2 - 1));//0437
            return;
        }
    }

    if (arr[y0][x0] == 1)
        result.first++;
    else
        result.second++;

    return;
}

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;

    cin >> N;
    for (int i = 0; i < N; i++)
        for (int k = 0; k < N; k++)
            cin >> arr[i][k];

    DFS(N, 0, 0, N - 1, N - 1);
    cout << result.second << '\n' << result.first << '\n';

    return 0;
}
