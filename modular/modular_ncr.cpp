const long long N = 3e5 + 10, MOD = 1e9 + 7;
long long fact[N];

// Calculates (a ^ b) mod p
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

/*
    (a^-1) % p
    a and p should be co-prime
*/
long long mod_inverse(long long a, long long p)
{
    return modular_exponentiation(a, p - 2, p);
}

// calculates factorial [1, n) (excluding n)
void calc_facts(long long n, long long p)
{
    fact[0] = 1;
    for (long long i = 1; i < n; i++)
        fact[i] = (i * fact[i - 1]) % p;
    return;
}

long long calc_ncr(long long n, long long r, long long p)
{
    if (n < r)
        return 0;
    long long res = fact[n];
    res = (res * mod_inverse(fact[r], p)) % p;
    res = (res * mod_inverse(fact[n - r], p)) % p;
    return res;
}
