#include "lib.h"

int ff(int x) {
  return 2 / x;
}

int main() {
  return myfun(1, ff) != ff(10);
}
