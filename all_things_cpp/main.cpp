#include <iostream>
#include <typeinfo>
#include <fstream>
#include <vector>
#include <array>
#include "utils.h"

void print_string(std::string item, bool end)
{
    if (end)
    {
        std::cout << item << std::endl;
    }
    else
    {
        std::cout << item;
    }
}

void print_int(int item, bool end)
{
    if (end)
    {
        std::cout << item << std::endl;
    }
    else
    {
        std::cout << item;
    }
}

void hello_world()
{
    print_string("Hello World!", true);
}

void print_array(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << array[i] << ' ';
    }
    std::cout << '\n';
}

void print_vector(std::vector<int> &vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        std::cout << vec[i] << ' ';
    }
    std::cout << '\n';
}

void get_vector(std::vector<int> vec)
{
    print_vector(vec);
}

void string_tests()
{
    std::string name;
    print_string("enter your name: ", false);
    getline(std::cin, name);
    print_string("hello ", false);
    print_string(name, true);
}

void sizes()
{
    std::cout << __INT_MAX__ << std::endl;
    std::cout << __SIZEOF_DOUBLE__ << std::endl;
    std::cout << std::fixed << __DBL_MAX__ << std::endl;
}

void factorial()
{
    int num;
    std::cout << "enter a number: ";
    std::cin >> num;

    for (int i = num - 1; i > 1; i--)
    {
        num *= i;
    }
    std::cout << std::fixed << num << std::endl;
}

void array_tests()
{
    int len;
    print_string("enter length of the array: ", false);
    std::cin >> len;

    int nums[len];
    for (int i = 0; i < len; i++)
    {
        std::cin >> nums[i];
    }

    std::cout << "{";

    for (int i = 0; i < len; i++)
    {
        std::cout << nums[i] << ", ";
    }

    std::cout << "}";
}

void vector_tests()
{
    std::vector<int> vec = {1, 2, 3, 4, 5};

    vec.push_back(42);
    print_int(vec.size(), true);
    print_vector(vec);

    vec.pop_back();
    print_vector(vec);

    std::vector<int>::iterator i;
    i = vec.begin() + 2; // vec.end() to access last element
    std::cout << *i << std::endl;
    
    vec.erase(i);
    print_int(vec.size(), true);
    print_vector(vec);
}

void file_tests()
{
    std::string filename;
    print_string("enter file name: ", false);
    getline(std::cin, filename);

    std::ofstream file(filename, std::ios::app);
    file << "Hello World!\n";
    file.close();
}

void do_smthng(int array[], int size)
{
    print_array(array, size);
}

template <typename T>
void swap(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

template <typename T>
void swap(T a[], T b[], T size)
{
    for (int i = 0; i < size; i++)
    {
        T temp = a[i];
        a[i] = b[i];
        b[i] = temp;
    }
}

struct Rectangle_s
{
    int length;
    int width;
};

class Rectangle_c
{
    static int iterator;

public:
    int length;
    int width;

    static int get_iterator()
    {
        return iterator;
    }

    Rectangle_c()
    {
        // std::cout << "constructor" << std::endl;
        iterator++;
    }

    Rectangle_c(int length, int width)
    {
        this->length = length;
        this->width = width;
        iterator++;
    }

    ~Rectangle_c()
    {
        // std::cout << "destructor" << std::endl;
        iterator--;
    }
};

int Rectangle_c::iterator = 0;

int get_area(int length, int width)
{
    return length * width;
}

void class_tests()
{
    Rectangle_c rect0;
    rect0.length = 20;
    rect0.width = 10;

    Rectangle_c rect1(30, 20);

    std::cout << rect0.length << '\n';
    std::cout << rect1.length << '\n';

    std::cout << get_area(rect0.length, rect0.width) << std::endl;
    std::cout << get_area(rect1.length, rect1.width) << std::endl;

    std::cout << Rectangle_c::get_iterator() << std::endl;
    rect0.~Rectangle_c();
    std::cout << Rectangle_c::get_iterator() << std::endl;
}

class Point
{
private:
    int hidden = 100;

public:
    int x = 10;
    int y = 20;

    Point operator+(Point p)
    {
        Point new_point;
        new_point.x = x + p.x;
        new_point.y = y + p.y;
        return new_point;
    }

    bool operator==(Point p)
    {
        if (x == p.x && y == p.y)
        {
            return true;
        }
    }

    friend void get_hidden(Point p);
};

void get_hidden(Point p)
{
    std::cout << p.hidden << std::endl;
}

void friend_fn()
{
    Point p1;
    get_hidden(p1);
}

std::ostream &operator<<(std::ostream &output, Point &p)
{
    output << "x: " << p.x << " y: " << p.y;
    return output;
}

std::istream &operator>>(std::istream &input, Point &p)
{
    input >> p.x >> p.y;
    return input;
}

void operator_overload()
{
    Point p1, p2;
    Point p3 = p1 + p2;
    Point p4;

    std::cin >> p4;
    std::cout << (p1 == p2) << std::endl;
    // std::cout << p3.x << ' ' << p3.y << std::endl;
    std::cout << p3 << std::endl;
    std::cout << p4 << std::endl;
}

void class_across_files()
{
    Dummy dummy1(1);
    dummy1.print_value();
    std::cout << dummy1.value << std::endl;
}

int main()
{
    hello_world();
    // string_tests();
    // sizes();
    // factorial();
    // array_tests();
    // vector_tests();
    // file_tests();

    // int data[] = {1, 2, 3};
    // do_smthng(data, 3);

    // std::cout << utilz::power(3, 3) << std::endl;

    // std::string a = "a";
    // std::string b = "b";
    // swap(a, b);
    // std::cout << a << ' ' << b << std::endl;

    // std::vector<int> a = {1, 2, 3};
    // std::vector<int> b;
    // print_vector(a);
    // print_vector(b);
    // b = a;
    // print_vector(b);

    // int a[] = {1, 2, 3};
    // int b[] = {4, 5, 6};
    // swap(a, b, 3);
    // print_array(a, 3);
    // print_array(b, 3);

    // class_tests();
    // operator_overload();
    // friend_fn();
    // class_across_files();

    return 0;
}
