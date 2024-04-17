#include <iostream>

void print_flag() {
    std::cout << "The flag is: " << '\x44' << '\x65' << '\x42' << '\x55';
    std::cout << '\x67' << '\x2d' << '\x6d' << '\x45' << '\n';
}

int main() {
    if (volatile bool check = true) print_flag();
    else std::cout << "You won't be getting the flag that way!\n";
}
