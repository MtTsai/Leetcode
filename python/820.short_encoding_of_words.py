class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        tree = {}
        for w in words:
            trie = tree
            for c in reversed(w):
                if c not in trie.keys():
                    trie[c] = {}
                trie = trie[c]
        
        self.ans = 0
        def dfs(trie, depth):
            if len(trie):
                for key in trie:
                    dfs(trie[key], depth + 1)
            else:
                self.ans += depth + 1
            
        dfs(tree, 0)
        return self.ans
