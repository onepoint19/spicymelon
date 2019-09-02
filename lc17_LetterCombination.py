class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {}
        dic = {2: ['a','b', 'c'],
                 3: ['d', 'e', 'f'],
                 4: ['g', 'h', 'i'],
                 5: ['j', 'k', 'l'],
                 6: ['m', 'n', 'o'],
                 7: ['p', 'q', 'r', 's'],
                 8: ['t', 'u', 'v'],
                 9: ['w', 'x', 'y', 'z']}    
        
        # print(dic)
        r = self.comb(dic,digits)
        r.sort()
        return r
        
    def comb(self, dic,digits):
        if digits == "":
            return []
        if len(digits) == 1:
            print(digits[0])

            return [x for x in dic[int(digits[0])]]
        temp = self.comb(dic,digits[0:len(digits)-1])
        ans = []
        for i in dic[int(digits[len(digits)-1])]:
            for x in temp:
                ans.append(x+str(i))
        return ans

                
        
            
