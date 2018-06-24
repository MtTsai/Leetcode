class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        s = len(wordList)
        wordList.append(beginWord)

        if endWord in wordList:
            e = wordList.index(endWord)
        else:
            return 0

        wordlen = len(beginWord)

        dep = 1
        curr, back = set([s]), set([e])
        queue = set([s])

        while True:
            dep += 1
            tmp = set()
            for node in curr:
                tWord = wordList[node]
                possible_word = set([tWord[:idx] + ch + tWord[idx+1:] for idx in range(wordlen) for ch in 'abcdefghijklmnopqrstuvwxyz'])
                for idx, str in enumerate(wordList):
                    if idx not in queue:
                        if wordList[idx] in possible_word:
                            tmp.add(idx)

            if not tmp:
                return 0
            else:
                curr = tmp

                if curr & back:
                    return dep

                if len(curr) > len(back):
                    curr, back = back, curr

                queue = queue.union(curr)
