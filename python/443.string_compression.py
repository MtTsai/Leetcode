class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        ch = chars[0]
        count = 0
        clen = len(chars)
        for i in range(clen):
            c = chars[i]
            if c != ch:
                chars.append(ch)
                if count > 1:
                    for int_ch in str(count):
                        chars.append(int_ch)
                count = 1
                ch = c
            else:
                count += 1
        chars.append(str(ch))
        if count > 1:
            for int_ch in str(count):
                chars.append(int_ch)

        for _ in range(clen):
            chars.pop(0)

        return len(chars)
