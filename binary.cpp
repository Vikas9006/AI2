#include <bits/stdc++.h>
using namespace std;
#define ll long long

// bits are starting from 0
ll get_bit(ll n, ll bit)
{
    return ((n & (1 << bit)) != 0);
}

ll set_bit(ll n, ll bit)
{
    return (n | (1 << bit));
}

ll clear_bit(ll n, ll bit)
{
    ll mask = ~(1 << bit);
    return (n & mask);
}

ll update_bit(ll n, ll bit, ll val)
{
    ll mask = ~(1 << bit);
    n = (n & mask);
    return (n | (val << bit));
}

vector<ll> binaryVal(ll n, ll totalBits)
{
    vector<ll> v(totalBits, 0);
    for (ll i = 0; i < totalBits; i++)
        if ((n & (1 << i)) != 0)
            v[i] = 1;
    return v;
}

ll numBits(ll n)
{
    ll counting = 0;
    while (n > 0)
    {
        n = n >> 1;
        counting++;
    }
    return counting;
}
