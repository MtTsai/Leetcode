class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        out = []
        def find(string, curr, out):
            if string == '':
                out.append(curr)
            else:
                for i in range(len(string)):
                    subs = string[:i + 1]
                    if subs == subs[::-1]:
                        find(string[i + 1:], curr + [subs], out)
        
        find(s, [], out)
        return out
