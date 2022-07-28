#include <iostream>

using namespace std;

void func(int num);

void func(int num)
{
  if (num == 0) {
    cout << "No arguments provided\n";
  } else if (num == 0) { // intentional mistake
    cout << "1 argument provided\n";
  } else if (num == 2) {
    cout << "2 arguments provided\n";
  } else {
    cout << num << " arguments provided\n";
  }
//   if (argv != 0) {
//     cout << "argv not null\n";; // intentional extra-semicolon
//   }
//   if (argv == nullptr) {
//     return **argv; // intentional nullptr dereference
//   }
}

int main(int argc, char* argv[]) {
//   int num = argc - 1;
  func(0);
  
  func(2);
  
  

  return 0;
}
