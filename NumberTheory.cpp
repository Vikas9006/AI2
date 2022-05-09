#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool isPrime(int n)
{
    // Corner case
    if (n <= 1)
        return false;

    // Check from 2 to sqrt(n)
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;

    return true;
}