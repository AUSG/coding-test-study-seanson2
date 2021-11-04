#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int M;
    int S = 0;
    string buf;

    cin >> M;
    for (int i = 0; i < M; i++)
    {
        int X;
        bool tmp;

        cin >> buf;
        if (buf.compare("all") == 0) {
            S = (1 << 21) - 1;
            continue;
        }
        else if (buf.compare("empty") == 0) {
            S = 0;
            continue;
        }

        cin >> X;
        switch (buf[0])
        {
        case 'a':
            S = S | (1 << X);
            break;
        case 'r':
            S = S & ~(1 << X);
            break;
        case 'c':
            tmp = S & (1 << X);
            cout << tmp << '\n';
            break;
        case 't':
            S = S ^ (1 << X);
            break;
        }
    }

    return 0;
}
