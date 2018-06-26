class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
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
                return [[]]
            if type(dp[start]) is list:
                return dp[start]
            
            trie = tree
            dp[start] = []
            for i in range(start, len(s)):
                c = s[i]
                if c in trie:
                    trie = trie[c]
                    
                    if '#' in trie:
                        ret = find(s, i + 1, tree, dp)
                        dp[start] += [[s[start:i + 1]] + str_list for str_list in ret]
                else:
                    break

            return dp[start]
        
        no_visit_dp = [0] * len(s)

        return [' '.join(str_list) for str_list in find(s, 0, tree, no_visit_dp)]
