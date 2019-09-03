class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def gen(left, right, prefix):
            a = []
            if left == 0 or right == 0:
                a.append(prefix+"("*left + ")"*right)
                return a
            
            elif left < right:
                prefix1 = prefix + "("
                prefix2 = prefix + ")"
                for x in gen(left-1, right, prefix1):
                    a.append(x)
                    
                for x in gen(left, right-1, prefix2):
                    a.append(x)
                return a
            
            elif left == right:
                prefix1 = prefix + "("
                for x in gen(left-1, right, prefix1):
                    a.append(x)
                return a

        result = gen(n,n,"")
        return result
    
