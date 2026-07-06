class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Hash_s, Hash_t = {},{}
        for i in range(len(s)):
            Hash_s[s[i]] = 1 + Hash_s.get(s[i], 0)
            Hash_t[t[i]] = 1 + Hash_t.get(t[i], 0)
        
        for itm in Hash_s:
            if Hash_s[itm] != Hash_t.get(itm, 0):
                return False
        
        return True