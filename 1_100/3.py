class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_set = set()
        res_len = 0
        # 右指针
        right = 0
        for i in range(len(s)):
            # i为左指针
            if i != 0:
                # 能进到这里面，要么就是右指针到最右边，要么就是右指针遇到重复的元素
                res_set.remove(s[i-1])
            while right < len(s) and s[right] not in res_set:
                res_set.add(s[right])
                right += 1
                res_len = max(res_len, right - i)
        return res_len
print(Solution().lengthOfLongestSubstring("abcabcbb"))

