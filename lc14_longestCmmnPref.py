class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        elif len(strs)==1:
            return strs[0]
        key = strs[0]
        for x in strs:
            if len(x)< len(key):
                key = x
        for x in strs:
            i = 0
            if key == "":
                return ""
            while i < len(key):
                if x[i] != key[i]:
                    break
                i += 1
            key = key[0:i]
        return key
