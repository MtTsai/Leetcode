import collections

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        if len(num) == k:
            return "0"


        rm_id = []
        prev = collections.deque([])
        for i in range(len(num)):
            while prev and num[prev[-1]] > num[i]:
                rm_id.append(prev[-1])
                prev.pop()
                if len(rm_id) == k:
                    break
            prev.append(i)
            if len(rm_id) == k:
                break

        while len(rm_id) < k:
            rm_id.append(prev[-1])
            prev.pop()

        out = ''.join([c for i, c in enumerate(num) if i not in rm_id])

        lead = 0
        while len(out) - lead > 1 and out[lead] == "0":
            lead += 1

        return out[lead:]

if __name__ == "__main__":
    data = [("1219", "1432219", 3),
            ("11", "1432219", 5),
            ("200", "10200", 1),
            ("0", "10", 2),
            ("0", "10", 1)]

    for ans, num, k in data:
        out = Solution().removeKdigits(num, k)
        if out != ans:
            print "Expect: {}".format(ans)
            print "Output: {}".format(out)
            print "Nums: {}, K: {}".format(num, k)
    print "Done"

