class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def is_upper(c):
            return True if c >= 'A' and c <= 'Z' else False

        if is_upper(word[0]):
            if len(word) >= 2:
                for c in word[2:]:
                    if is_upper(c) != is_upper(word[1]):
                        return False
                return True
            else:
                return True
        else:
            for c in word[1:]:
                if is_upper(c):
                    return False
            return True
                
