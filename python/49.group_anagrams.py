class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        out_dict = {}
        out = []
        for string in strs:
            key = ''.join(sorted(string))
            if key in out_dict:
                idx = out_dict[key]
                out[idx].append(string)
            else:
                out_dict[key] = len(out)
                out.append([string])
        return out
