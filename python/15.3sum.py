class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def merge(a, b):
            ai = bi = 0
            ret = []
            while ai != len(a):
                if bi != len(b):
                    if a[ai] < b[bi]:
                        ret.append(a[ai])
                        ai += 1
                    else:
                        ret.append(b[bi])
                        bi += 1
                else:
                    ret += a[ai:]
                    break
            if bi != len(b):
                ret += b[bi:]
            return ret
        
        def msort(l):
            llen = len(l)
            if llen <= 1:
                return l
            else:
                return merge(msort(l[:llen/2]), msort(l[llen/2:]))

        nums = msort(nums)
        nlen = len(nums)
        ans = []
        for i in range(0, nlen - 2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue

            l, r = i + 1, nlen - 1
            
            while l < r:
                y, z = nums[l], nums[r]

                if x + y + z > 0:
                    r -= 1
                    while l < r and nums[r] == z:
                        r -= 1
                elif x + y + z < 0:
                    l += 1
                    while l < r and nums[l] == y:
                        l += 1
                else:
                    ans.append([x,y,z])
                    
                    r -= 1
                    l += 1

                    while l < r and nums[r] == z:
                        r -= 1
                    while l < r and nums[l] == y:
                        l += 1

        return ans
