class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        T_accu_tbl = {}
        for c in t:
            if c in T_accu_tbl.keys():
                T_accu_tbl[c] += 1
            else:
                T_accu_tbl[c] = 1

        kind_not_found = len(T_accu_tbl)

        S_queue = {}
        S_queue_mix = []

        start_idx = 0
        min_len = 0
        min_win = ""

        for i in range(len(s)):
            c = s[i]
            if c in T_accu_tbl.keys():
                S_queue_mix.append(i)

                if c in S_queue.keys():
                    S_queue[c] += 1
                else:
                    S_queue[c] = 1

                if kind_not_found:
                    if S_queue[c] == T_accu_tbl[c]:
                        kind_not_found -= 1

                        if not kind_not_found:
                            min_len = i - S_queue_mix[start_idx]
                            min_win = s[S_queue_mix[start_idx] : S_queue_mix[-1] + 1]

                if not kind_not_found:
                    while True:
                        start_c = s[S_queue_mix[start_idx]]
                        if S_queue[start_c] > T_accu_tbl[start_c]:
                            start_idx += 1
                            S_queue[start_c] -= 1

                            if i - S_queue_mix[start_idx] < min_len:
                                min_len = i - S_queue_mix[start_idx]
                                min_win = s[S_queue_mix[start_idx] : S_queue_mix[-1] + 1]
                        else:
                            break

        return min_win

if __name__ == "__main__":
    data = [("BANC", "ADOBECODEBANC", "ABC"),
            ("ba", "bba", "ab")]

    for ans, S, T in data:
        out = Solution().minWindow(S, T)
        if out != ans:
            print "S: {}".format(S)
            print "T: {}".format(T)
            print "Expect: {}".format(ans)
            print "Output: {}".format(out)
    print "Done"
