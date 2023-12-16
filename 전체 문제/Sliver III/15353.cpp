#include <string>
#include <iostream>

using namespace std;

string solution(string a, string b) {
    int q = min(a.length(), b.length());
    string s, l;

    if (q == a.length()) { s = a; l = b; }
    else { s = b; l = a; }

    int j = l.length() - 1;

    for (int i = s.length() - 1; i >= 0; i--, j--) {
        l[j] += s[i] - '0';
    }

    for (int i = l.length() - 1; i > 0; i--) {
        if (l[i] - '0' > 9) { l[i-1]++; l[i] = (l[i] - '0') % 10 + '0'; }
    }

    if (l[0] - '0' > 9) { l[0] = (l[0] - '0') % 10 + '0'; l = "1" + l; }

    return l;
}

int main() {
  string a, b;
  cin >> a >> b;
  cout << solution(a, b);
  return 0;
}
