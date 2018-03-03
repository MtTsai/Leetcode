class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        words = set(words)
        ly = len(board)
        lx = len(board[0]) if ly > 0 else 0
        board_azmap = {}
        word_trie = {}

        for row in range(ly):
            for col in range(lx):
                c, pos = board[row][col], (col, row)
                if c in board_azmap.keys():
                    board_azmap[c].append(pos)
                else:
                    board_azmap[c] = [pos]

        for _word in words:
            trie_ref = word_trie
            for c in _word:
                if c not in trie_ref.keys():
                    trie_ref[c] = {}

                trie_ref = trie_ref[c]
            trie_ref['_'] = _word

        def searchWords(trie_ref, (x, y), trace):
            if x < 0 or x >= lx or y < 0 or y >= ly or trace[y][x] or board[y][x] not in trie_ref.keys():
                ret = []
            else:
                trace[y][x] = 1

                up, down, left, right = searchWords(trie_ref[board[y][x]], (x, y - 1), trace), \
                                        searchWords(trie_ref[board[y][x]], (x, y + 1), trace), \
                                        searchWords(trie_ref[board[y][x]], (x - 1, y), trace), \
                                        searchWords(trie_ref[board[y][x]], (x + 1, y), trace)

                trace[y][x] = 0

                ret = up + down + left + right

            return ret + [trie_ref['_']] if '_' in trie_ref.keys() else ret

        ans = []
        for _1st_char in word_trie.keys():
            if _1st_char not in board_azmap.keys():
                continue

            for _x, _y in board_azmap[_1st_char]:
                tracemap = [[0 for x in range(lx)] for y in range(ly)]
                ans += searchWords(word_trie, (_x, _y), tracemap)

        return list(set(ans))

if __name__ == "__main__":
    inputPool = [(["oath", "eat"], ["oath","pea","eat","rain"], [['o','a','a','n'],
                                                                 ['e','t','a','e'],
                                                                 ['i','h','k','r'],
                                                                 ['i','f','l','v']]),
                 (['a'],           ["a", "a"],                  [['a']]),
                 ([],              ["aaa"] ,                    [['a','a']]),
                 (["aabbbbabbaababaaaabababbaaba",
                   "abaabbbaaaaababbbaaaaabbbaab",
                   "ababaababaaabbabbaabbaabbaba"],
                                   ["bbaabaabaaaaabaababaaaaababb",
                                    "aabbaaabaaabaabaaaaaabbaaaba",
                                    "babaababbbbbbbaabaababaabaaa",
                                    "bbbaaabaabbaaababababbbbbaaa",
                                    "babbabbbbaabbabaaaaaabbbaaab",
                                    "bbbababbbbbbbababbabbbbbabaa",
                                    "babababbababaabbbbabbbbabbba",
                                    "abbbbbbaabaaabaaababaabbabba",
                                    "aabaabababbbbbbababbbababbaa",
                                    "aabbbbabbaababaaaabababbaaba",
                                    "ababaababaaabbabbaabbaabbaba",
                                    "abaabbbaaaaababbbaaaaabbbaab",
                                    "aabbabaabaabbabababaaabbbaab",
                                    "baaabaaaabbabaaabaabababaaaa",
                                    "aaabbabaaaababbabbaabbaabbaa",
                                    "aaabaaaaabaabbabaabbbbaabaaa",
                                    "abbaabbaaaabbaababababbaabbb",
                                    "baabaababbbbaaaabaaabbababbb",
                                    "aabaababbaababbaaabaabababab",
                                    "abbaaabbaabaabaabbbbaabbbbbb",
                                    "aaababaabbaaabbbaaabbabbabab",
                                    "bbababbbabbbbabbbbabbbbbabaa",
                                    "abbbaabbbaaababbbababbababba",
                                    "bbbbbbbabbbababbabaabababaab",
                                    "aaaababaabbbbabaaaaabaaaaabb",
                                    "bbaaabbbbabbaaabbaabbabbaaba",
                                    "aabaabbbbaabaabbabaabababaaa",
                                    "abbababbbaababaabbababababbb",
                                    "aabbbabbaaaababbbbabbababbbb",
                                    "babbbaabababbbbbbbbbaabbabaa"],
                                                                [["b","a","a","b","a","b"],
                                                                 ["a","b","a","a","a","a"],
                                                                 ["a","b","a","a","a","b"],
                                                                 ["a","b","a","b","b","a"],
                                                                 ["a","a","b","b","a","b"],
                                                                 ["a","a","b","b","b","a"],
                                                                 ["a","a","b","a","a","b"]]),
                 (['aaaaaaaaaaaaaadh',
                   'aaaaaaaaaaaaaadc',
                   'aaaaaaaaaaaaaade',
                   'aaaaaaaaaaaaaaaa',
                   'aaaaaaaaaaaaaaac',
                   'aaaaaaaaaaaaaaab',
                   'aaaaaaaaaaaaaaae',
                   'aaaaaaaaaaaaaaad',
                   'aaaaaaaaaaaaaaei',
                   'aaaaaaaaaaaaaaed',
                   'aaaaaaaaaaaaaabc',
                   'aaaaaaaaaaaaaabf',
                   'aaaaaaaaaaaaaacb',
                   'aaaaaaaaaaaaaacg',
                   'aaaaaaaaaaaaaacd'],
                                   ["a" * 14 + c1 + c2 for c1 in 'abcdefghijkl' for c2 in 'abcdefghijklmnopqrstuvwxyz'],
                                                                [["a","a","a","a"],
                                                                 ["a","a","a","a"],
                                                                 ["a","a","a","a"],
                                                                 ["a","a","a","a"],
                                                                 ["b","c","d","e"],
                                                                 ["f","g","h","i"],
                                                                 ["j","k","l","m"],
                                                                 ["n","o","p","q"],
                                                                 ["r","s","t","u"],
                                                                 ["v","w","x","y"],
                                                                 ["z","z","z","z"]])
                ]

    for _ans, _words, _board in inputPool:
        result = Solution().findWords(_board, _words)
        if sorted(result) != sorted(_ans):
            print "Fail"
            print "Output: {}".format(result)
            print "Expect: {}".format(_ans)

    print "Done"
