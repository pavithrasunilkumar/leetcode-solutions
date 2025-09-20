#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n == 0) return "";

        // Preprocess: insert '#' between characters to handle even length
        string t = "#";
        for (char c : s) {
            t += c;
            t += "#";
        }

        int m = t.size();
        vector<int> p(m, 0);  // Array to store palindrome radius
        int c = 0, r = 0;     // Current center and right boundary
        int maxLen = 0, centerIndex = 0;

        for (int i = 0; i < m; ++i) {
            int mirr = 2 * c - i;  // Mirror of i with respect to center c
            if (i < r) p[i] = min(r - i, p[mirr]);

            // Expand around center i
            while (i + p[i] + 1 < m && i - p[i] - 1 >= 0 && t[i + p[i] + 1] == t[i - p[i] - 1])
                ++p[i];

            // Update center and right boundary
            if (i + p[i] > r) {
                c = i;
                r = i + p[i];
            }

            // Track maximum palindrome
            if (p[i] > maxLen) {
                maxLen = p[i];
                centerIndex = i;
            }
        }

        int start = (centerIndex - maxLen) / 2; // Map back to original string
        return s.substr(start, maxLen);
    }
};
