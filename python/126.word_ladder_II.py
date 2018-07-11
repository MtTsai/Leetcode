class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        for idx in range(len(wordList)):
            if wordList[idx] == beginWord:
                wordList.pop(idx)
                break
        tree = {}
        for idx in range(len(wordList)):
            w = wordList[idx]
            trie = tree
            for c in w:
                if c not in trie.keys():
                    trie[c] = {}
                trie = trie[c]
            trie['#'] = idx

        trie = tree
        for c in endWord:
            if c not in trie:
                return []
            trie = trie[c]
        end_idx = trie['#']
            
        def next_idx(w, tree):
            out = []
            for i in range(len(w)):
                trie = tree
                pre = 0
                find = True
                while pre < i:
                    c = w[pre]
                    if c not in trie:
                        find = False
                        break
                    trie = trie[c]
                    pre += 1

                if not find:
                    continue

                for mid_c in trie.keys():
                    if mid_c == w[i]:
                        continue
                    post_trie = trie[mid_c]
                    find = True
                    for j in range(i + 1, len(w)):
                        c = w[j]
                        if c not in post_trie:
                            find = False
                            break
                        post_trie = post_trie[c]
                    if find:
                        out.append(post_trie['#'])  
            return out
             
        self.ans = []
        self.min = len(wordList) + 1
        self.dp = {}
        self.visit = [0] * len(wordList)
        def dfs(end_idx, tree, ladder):
            if ladder[-1] == end_idx:
                if len(ladder) == self.min:
                    self.ans.append(ladder)
                elif len(ladder) < self.min:
                    self.min = len(ladder)
                    self.ans = [ladder]

            if len(ladder) < self.min:
                if ladder[-1] not in self.dp.keys():
                    self.dp[ladder[-1]] = next_idx(wordList[ladder[-1]], tree)
                next_idx_list = self.dp[ladder[-1]]
                for nid in next_idx_list:
                    if nid not in ladder:
                        dfs(end_idx, tree, ladder + [nid])

        def bfs(end_idx, tree, ladders):
            if ladders:
                find = False
                for ladder in ladders:
                    if ladder[-1] == end_idx:
                        find = True
                        self.ans.append(ladder)
                if find:
                    return

                new_ladders = []
                new_visit = []
                for ladder in ladders:
                    if ladder[-1] not in self.dp.keys():
                        self.dp[ladder[-1]] = next_idx(wordList[ladder[-1]], tree)
                    next_idx_list = self.dp[ladder[-1]]
                    for nid in next_idx_list:
                        if not self.visit[nid]:
                            new_visit.append(nid)
                            new_ladders.append(ladder + [nid])
                for v_idx in new_visit:
                    self.visit[v_idx] = 1
                bfs(end_idx, tree, new_ladders)

        bfs(end_idx, tree, [[nid] for nid in next_idx(beginWord, tree)])
        out = []
        for row in self.ans:
            out.append([beginWord] + [wordList[idx] for idx in row])
        return out

        # dfs is Time Limit Exceed
        for nid in next_idx(beginWord, tree):
            dfs(end_idx, tree, [nid])

        out = []
        for row in self.ans:
            out.append([beginWord] + [wordList[idx] for idx in row])
        return out
