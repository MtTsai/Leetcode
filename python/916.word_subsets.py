class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        b_all = {}
        for b in B:
            b_dict = {}
            for c in b:
                if c in b_dict:
                    b_dict[c] += 1
                else:
                    b_dict[c] = 1
            for c in b_dict:
                if c in b_all:
                    b_all[c] = max(b_all[c], b_dict[c])
                else:
                    b_all[c] = b_dict[c]
        ans = []

        for a in A:
            a_dict = {}
            for c in a:
                if c in b_all:
                    if c in a_dict:
                        a_dict[c] += 1
                    else:
                        a_dict[c] = 1
            for c in b_all:
                if c not in a_dict:
                    break
                if a_dict[c] < b_all[c]:
                    break
            else:
                ans.append(a)
        return ans
