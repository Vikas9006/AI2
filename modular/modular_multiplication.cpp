// (a * b) % p
long long mod_mul(long long a, long long b, long long p)
{
    a = a % p;
    b = b % p;
    return (a * b) % p;
}