#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

long long operations = 0;
int maxDepth = 0;

void complexRec(int n, int depth) {

    maxDepth = max(maxDepth, depth);

    if (n <= 2) {
        operations++;
        return;
    }

    int p = n;
    while (p > 0) {
        vector<int> temp(n);
        operations++;

        for (int i = 0; i < n; i++) {
            temp[i] = i ^ p;
            operations++;
        }
        p >>= 1;
        operations++;
    }

    vector<int> small(n);
    for (int i = 0; i < n; i++) {
        small[i] = i * i;
        operations++;
    }

    reverse(small.begin(), small.end());
    operations += n;

    complexRec(n / 2, depth + 1);
    complexRec(n / 2, depth + 1);
    complexRec(n / 2, depth + 1);
}

int main() {

    vector<int> testSizes = {8, 16, 32, 64, 128};

    for (int n : testSizes) {

        operations = 0;
        maxDepth = 0;

        auto start = high_resolution_clock::now();
        complexRec(n, 1);
        auto stop = high_resolution_clock::now();

        auto duration = duration_cast<milliseconds>(stop - start);

        cout << "n = " << n << endl;
        cout << "Operations = " << operations << endl;
        cout << "Recursion Depth = " << maxDepth << endl;
        cout << "Time Taken = " << duration.count() << " ms\n\n";
    }

    return 0;
}