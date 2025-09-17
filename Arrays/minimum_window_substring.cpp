class Solution {
public:
    string minWindow(string s, string t) {
        if(s.empty() || t.empty()) return "";
        
        int dict_t[128] = {0}, window[128] = {0};
        for(char c : t) dict_t[c]++;
        
        int required = 0;
        for(int i = 0; i < 128; i++) if(dict_t[i] > 0) required++;
        
        int l = 0, r = 0, formed = 0;
        int min_len = INT_MAX, start = 0;
        
        while(r < s.size()){
            char c = s[r];
            window[c]++;
            if(dict_t[c] > 0 && window[c] == dict_t[c]) formed++;
            
            while(l <= r && formed == required){
                if(r - l + 1 < min_len){
                    min_len = r - l + 1;
                    start = l;
                }
                char d = s[l];
                window[d]--;
                if(dict_t[d] > 0 && window[d] < dict_t[d]) formed--;
                l++;
            }
            r++;
        }
        
        return min_len == INT_MAX ? "" : s.substr(start, min_len);
    }
};
