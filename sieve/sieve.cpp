#include <vector>
using namespace std;
const long long N = 1e5 + 10;


// From here
long long sieve[N];

// Runs sieve from [2, n) (excluding n)
void run_sieve(long long n)
{
    for (long long i = 0; i < n; i++)
        sieve[i] = i;
    for (long long i = 2; i < n; i++)
    {
        if (sieve[i] != i)
            continue;
        for (long long j = i * i; j < n; j += i)
            sieve[j] = i;
    }
    return;
}

vector<long long> primeFactors(long long x)
{
    vector<long long> ret;
    while (x > 1)
    {
        ret.push_back(sieve[x]);
        x = x / sieve[x];
    }
    return ret;
}

vector<pair<long long, long long>> primeFactorsPowers(long long x)
{
    vector<pair<long long, long long>> res;
    while (x > 1)
    {
        if (res.empty() || sieve[x] != res[res.size() - 1].first)
            res.push_back({sieve[x], 1});
        else
            (res[res.size() - 1].second)++;
        x = x/sieve[x];
    }
    return res;
}