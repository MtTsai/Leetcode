class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        out = []
        cnt = 1
        for w in S.split(" "):
            if not w:
                continue
            
            tmp = ""
            if w[0] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
                tmp += w + "ma"
            else:
                tmp += w[1:] + w[0] + "ma"
            
            tmp += "a" * cnt
            cnt += 1
            
            out.append(tmp)
            
        return " ".join(out)
