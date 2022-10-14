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
    uses Fermat’s little theorem
    a^(M - 1) ≅ 1 (mod M)
    a^(-1) ≅ a^(M - 2) (mod M)

*/
long long mod_inverse(long long a, long long p)
{
    return modular_exponentiation(a, p - 2, p);
}
