#include <bits/stdc++.h>
using namespace std;
#define ll long long
const long long MOD = 1e9 + 7;

// (a+b)%MOD
ll mod_add(ll a, ll b, ll n = MOD)
{
    a = a % n;
    b = b % n;
    return ((a + b) % n);
}

// (a-b)%MOD
ll mod_sub(ll a, ll b, ll n = MOD)
{
    a = a % n;
    b = b % n;
    return (a - b + n) % n;
}

// (a*b)%MOD
ll mod_mul(ll a, ll b, ll n = MOD)
{
    a = a % n;
    b = b % n;
    return (a * b) % n;
}

// (a^b)%MOD
ll mod_exp(ll a, ll b, ll n = MOD)
{
    ll res = 1;
    a = a % n;
    while (b > 0)
    {
        if ((b & 1) != 0)
            res = (res * a) % n;
        a = (a * a) % n;
        b = b >> 1;
    }
    return res;
}

// (a^-1)%MOD
// and and n should be co-prime
ll mod_inv(ll a, ll n = MOD)
{
    return mod_exp(a, n - 2);
}

ll mod_factorial(ll num, ll n = MOD)
{
    if (num < 0)
        return 0;
    ll res = 1;
    for (ll i = 2; i <= num; i++)
        res = (res * i) % MOD;
    return res;
}


ll ncr(ll n, ll r, ll mod = MOD)
{
    ll inv1 = mod_inv(mod_factorial(r));
    ll inv2 = mod_inv(mod_factorial(n - r));
    ll fact = mod_factorial(n);
    ll ans = fact;
    ans = mod_mul(ans, inv1);
    ans = mod_mul(ans, inv2);
    return ans;
}