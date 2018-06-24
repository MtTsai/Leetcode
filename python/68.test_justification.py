class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        linelen = 0
        linelist = []
        ans = []
        for w in words:
            if linelen + len(w) + len(linelist) > maxWidth:
                spacelen = maxWidth - linelen
                spacediv = len(linelist) - 1
                if spacediv:
                    for idx, wd in enumerate(linelist[:-1]):
                        if idx != spacediv and (spacelen % spacediv) > idx:
                            linelist[idx] += ' ' * ((spacelen / spacediv) + 1)
                        else:
                            linelist[idx] += ' ' * (spacelen / spacediv)
                            linelen = 0
                    ans.append(''.join(linelist))
                else:
                    ans.append(linelist[0] + ' ' * spacelen)
                linelist = [w]
                linelen = len(w)
            else:
                linelist.append(w)
                linelen += len(w)

        ans.append(' '.join(linelist))
        ans[-1] += ' ' * (maxWidth - len(ans[-1]))
            
        return ans
