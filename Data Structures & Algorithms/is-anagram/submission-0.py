class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_charset = {}
        s2_charset = {}

        for ch in s:
            if ch in s1_charset:
                s1_charset[ch] = s1_charset[ch] + 1
            else:
                s1_charset[ch] = 1
        
        for ch in t:
            if ch in s2_charset:
                s2_charset[ch] = s2_charset[ch] + 1
            else:
                s2_charset[ch] = 1
        
        if s1_charset == s2_charset:
            return True
        return False
        