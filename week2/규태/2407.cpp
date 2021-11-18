#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool check[101][101];
string memoStr[101][101];

string combination(int n, int r) {
    if (r == 0 || n == r) {
        memoStr[n][r] = '1';
        check[n][r] = true;
    }
    else if (r == 1) {
        memoStr[n][r] = to_string(n);
        check[n][r] = true;
    }

    if (check[n][r] == true)
        return memoStr[n][r];
    else
    {
        string num1 = combination(n - 1, r - 1);
        string num2 = combination(n - 1, r);

        int tmp1, tmp2, carry = 0, sum = 0;
        string result;

        if (num1.length() < num2.length()) {
            string tmp = num1;
            num1 = num2;
            num2 = tmp;
        }

        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        for (int i = 0; i < num1.length(); i++)
        {
            tmp1 = num1[i] - '0';
            if (i < num2.length())
                tmp2 = num2[i] - '0';
            else
                tmp2 = 0;
            sum = tmp1 + tmp2 + carry;
            if (sum > 9) {
                carry = 1;
                sum -= 10;
            }
            else
                carry = 0;
            result.push_back(sum + '0');
        }
        if (carry >= 1)
            result.push_back('1');

        reverse(result.begin(), result.end());
        check[n][r] = true;
        memoStr[n][r] = result;

        return memoStr[n][r];
    }
}

int main(void)
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n, r;

    cin >> n >> r;

    cout << combination(n, r) << '\n';

    return 0;
}
