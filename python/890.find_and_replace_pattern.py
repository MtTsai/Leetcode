class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        plen = len(pattern)
        
        def match(word):
            pmap = {}
            wmap = {}
            for i in range(plen):
                w = ord(word[i])
                p = ord(pattern[i])
                
                if p in pmap:
                    if pmap[p] != w:
                        return False
                else:
                    pmap[p] = w
                    if w in wmap:
                        return False
                    wmap[w] = p

            return True
        
        return [_w for _w in words if match(_w)]
