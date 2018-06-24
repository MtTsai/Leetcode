class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s != '' and (s[0] in ('-','+')):
            s = s[1:]
        sl = s.split('e')
        if len(sl) > 2:
            return False
        elif len(sl) == 2 and (sl[1] == '' or (sl[1][0] in ('-','+') and not sl[1][1:].isdigit()) or \
                                              (sl[1][0] not in ('-','+') and not sl[1].isdigit())):
            return False
        else:
            fsl = sl[0].split('.')
            if len(fsl) > 2:
                return False
            elif len(fsl) == 2:
                if fsl[0].isdigit() and fsl[1] == '':
                    return True
                elif fsl[1].isdigit() and fsl[0] == '':
                    return True
                elif fsl[0].isdigit() and fsl[1].isdigit():
                    return True
                else:
                    return False
            elif not fsl[0].isdigit():
                return False
                    
        return True
