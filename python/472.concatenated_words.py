class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        tree = {}
        for w in words:
            trie = tree
            for c in w:
                if c not in trie.keys():
                    trie[c] = {}
                trie = trie[c]
            trie["#"] = "#"

            
        def find(s, start, tree, dp, dp_w):
            if start == len(s):
                return 0
            if dp[start]:
                return dp[start]
            if s[start:] in dp_w.keys():
                return dp_w[s[start:]]
            trie = tree
            
            dp[start] = -len(words)
            for i in range(start, len(s)):
                c = s[i]
                if c in trie.keys():
                    trie = trie[c]
                else:
                    dp[start] = -len(words)
                    break
                if "#" in trie:
                    dp[start] = max(dp[start], find(s, i + 1, tree, dp, dp_w) + 1)
                    if dp[start] > 1:
                        break
                    
            return dp[start]
                
        out = []
        dp_w = {}
        for w in words:
            dp = [0] * len(w)
            
            ret = find(w, 0, tree, dp, dp_w)
            if len(w) > 200:
                dp_w[w] = ret
            if ret > 1:
                out.append(w)
                
        return out
