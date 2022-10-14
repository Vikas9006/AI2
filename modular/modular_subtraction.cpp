// (a-b)%MOD
long long mod_sub(long long a, long long b, long long p)
{
    a = a % p;
    b = b % p;
    return (a - b + p) % p;
}