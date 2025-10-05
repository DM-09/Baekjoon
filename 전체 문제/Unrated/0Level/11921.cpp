#include <cstdio>
using namespace std;

char inp[50000000];
int i = 0;

int read() {
  int v = 0;
  for (;inp[i]!='\n';i++) v = v*10 + inp[i]-'0';
  i++;
  return v;
}

int main() {
  int n = 0;
  long long sum = 0;
  
  fread(inp, 1, sizeof(inp), stdin);
  n = read();
  
  for (int j=0; j<n; j++) sum += read();
  
  printf("%d\n%lld", n, sum);
  return 0;
}
