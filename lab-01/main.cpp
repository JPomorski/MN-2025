#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

double f(double x) {
    return sqrt(pow(x, 2.0) + 1.0);
}

double g(double x) {
    return pow(x, 2.0) / (sqrt(pow(x, 2.0) + 1.0) + 1.0);
}

bool epsilon_float(float e) {
    return 1.0 == 1.0 + e;
}

bool epsilon_double(double e) {
    return 1.0 == 1.0 + e;
}

int main()
{
    double number_1 = 100000000000000.0001;
    double number_2 = 10.99;

    double expected = 20.99000000000000001;

    if (number_1 + number_2 == expected) {
        std::cout << "equal" << std::endl;
    } else {
        std::cout << "not equal" << std::endl;
    }

    std::cout << fixed << setprecision(20) << number_1 + number_2  << std::endl;

    std::cout << std::endl;

    // Z2

    double sum_2 = number_1 + number_2;
    double number_3 = 100000000000000.0;

    std::cout << fixed << setprecision(20) << sum_2 - number_3  << std::endl;

    // Z3

    std::cout << std::endl;

    float number_3_f = 10.000001;
    std::cout << fixed << setprecision(20) << number_3_f << std::endl;

    double number_3_d = 10.000001;
    std::cout << fixed << setprecision(20) << number_3_d << std::endl;

    std::cout << std::endl;

    // Z4

    double f_4 = 0.3 * 3.0 + 0.1;
    std::cout << f_4 << std::endl;

    std::cout << "Floor: " << floor(f_4) << std::endl;
    std::cout << "Ceil: " << ceil(f_4) << std::endl;

    std::cout << std::endl;

    // Z5

    double diff_5_1 = 1.0000001 - 1.0000000;
    double diff_5_2 = 1.0000002 - 1.0000001;

    std::cout << diff_5_1 << std::endl;
    std::cout << diff_5_2 << std::endl;

    std::cout << std::endl;

    // Z6

    double d_6_1 = 1.0 / 0.0;
    double d_6_2 = 0.0 / 0.0;

    std::cout << d_6_1 << std::endl;
    std::cout << d_6_2 << std::endl;

    std::cout << std::endl;

    // Z7?
    // int highest_float = 0;
    float e_f = 1.0;

    while(1 != 1 + e_f) {
        e_f = e_f / 2;
    }

    double e_d = 1.0;

    while(1 != 1 + e_d) {
        e_d = e_d / 2;
    }

    std::cout << "epsilon float: " << e_f << std::endl;
    std::cout << "epsilon double: " << e_d << std::endl;

    // for(int i = 0; i < 100000000; ++i) {
    //     if (epsilon_float(1.0 / i) == true) {
    //         highest_float = i;
    //         // std::cout << i << std::endl;
    //     }
    // }

    // int highest_double = 0;

    // for(int i = 0; i < 100000000; ++i) {
    //     if (epsilon_double(1.0 / i) == true) {
    //         highest_double = i;
    //         // std::cout << i << std::endl;
    //     }
    // }

    // std::cout << highest_float << std::endl;
    // std::cout << highest_double << std::endl;

    // std::cout << 1.0 + float(0.000000000000000001) << std::endl;

    std::cout << std::endl;

    // Z8

    double sum = 0;

    for (int i = 0; i < 1000000; ++i) {
        sum += 0.0001;
    }

    double sum_8 = 1000000 * 0.0001;

    if (sum == sum_8) {
        std::cout << "equal" << std::endl;
    } else {
        std::cout << "not equal" << std::endl;
    }

    std::cout << sum << std::endl;
    std::cout << sum_8 << std::endl;

    std::cout << std::endl;

    // Z9

    double sum_9 = 0;

    for (int i = 1; i <= 1000000; ++i) {
        sum_9 += 1.0/i;
    }

    double rev_sum_9 = 0;

    for (int i = 1000000; i >= 1; --i) {
        rev_sum_9 += 1.0/i;
    }

    if (sum_9 == rev_sum_9) {
        std::cout << "equal" << std::endl;
    } else {
        std::cout << "not equal" << std::endl;
    }

    std::cout << sum_9 << std::endl;
    std::cout << rev_sum_9 << std::endl;

    std::cout << std::endl;

    // Z10

    for (int i = -1; i >= -20; --i) {
        double f_10 = f(pow(8.0, i));
        double g_10 = g(pow(8.0, i));

        std::cout << "i = " << i << std::endl;

        std::cout << "f(x) = " << f_10 << std::endl;
        std::cout << "g(x) = " << g_10 << std::endl;

        std::cout << std::endl;
    }
}
