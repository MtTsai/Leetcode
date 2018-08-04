class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        regex = re.compile(r'\!|\?|\'|\,|\;|\.|\ ')
        
        wdict = {}
        for w_itr in regex.split(paragraph):
            w = w_itr.lower()
            if w and w not in banned:
                if w in wdict.keys():
                    wdict[w] += 1
                else:
                    wdict[w] = 1

        cnt = 0
        ans = ''
        for w in wdict.keys():
            if wdict[w] > cnt:
                cnt = wdict[w]
                ans = w
        return ans
