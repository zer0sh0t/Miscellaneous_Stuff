#include "utils.h"
#include <iostream>

namespace utilz
{
    double power(double base, int num)
    {
        double output = 1;
        for (int i = 0; i < num; i++)
        {
            output *= base;
        }
        return output;
    }
} // namespace utilz

Dummy::Dummy(int value)
{
    this->value = value;
}

void Dummy::print_value()
{
    std::cout << this->value << std::endl;
}
