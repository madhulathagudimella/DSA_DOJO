class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        p_count = {}
        window = {}
        result = []
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        for i in range(len(p)):
            window[s[i]] = window.get(s[i], 0) + 1
        if window == p_count:
            result.append(0)
        left = 0
        for right in range(len(p), len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            if window == p_count:
                result.append(left)
        return result