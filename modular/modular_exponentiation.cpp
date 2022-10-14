// Calculates (a^b) mod p
long long modular_exponentiation(long long a, long long b, long long p)
{
    a = a % p;
    long long res = 1;
    while (b)
    {
        if (b & 1)
            res = (res * a) % p;
        a = (a * a) % p;
        b = b >> 1;
    }
    return res;
}