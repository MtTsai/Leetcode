class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        def kmp_f(s):
            f = [0] * len(s) # Failure number
            i, j = 1, 0
            while i < len(s):
                if j == 0 or s[i - 1] == s[j - 1]:
                    f[i] = j
                    i += 1
                    j += 1
                else:
                    j = f[j]
            return f
        
        def kmp(f, s1, s2):
            if len(s1) > len(s2):
                return False

            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                elif i == 0:
                    j += 1
                else:
                    i = f[i]
                        
            return i == len(s1)

        f = kmp_f(B)
        reps = len(B) / len(A)
        if kmp(f, B, A):
            return 1
        if kmp(f, B, A*reps):
            return reps
        if kmp(f, B, A*(reps + 1)):
            return reps + 1
        if kmp(f, B, A*(reps + 2)):
            return reps + 2
        return -1
