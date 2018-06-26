class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        tree = {}
        for w in wordDict:
            trie = tree
            for c in w:
                if c not in trie.keys():
                    trie[c] = {}
                trie = trie[c]
            trie['#'] = '#'

        def find(s, start, tree, dp):
            if start == len(s):
                return True
            if dp[start]:
                return False
            
            trie = tree
            for i in range(start, len(s)):
                c = s[i]
                if c in trie:
                    trie = trie[c]
                    
                    if '#' in trie:
                        if find(s, i + 1, tree, dp):
                            return True
                        else:
                            dp[i + 1] = 1
                else:
                    return False
                
            return False
        
        no_visit_dp = [0] * len(s)

        return find(s, 0, tree, no_visit_dp)
