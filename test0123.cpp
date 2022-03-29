#include <iostream>

using namespace std;

// Lets define the first parent class.

class A
{

public:
    int x = 10;

    void Display_x_Variable()
    {
        cout << "The value of x is " << x << endl;
    }
};

//
/**
arrgc==> # of arguments to be passed.
argv = > Actual arguments
std:namespace
*/

int main(int argc, const char *argv[])
{
    A object_A;

    object_A.Display_x_Variable();

    return 0;
}