class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ans = []
        def ipaddr(n, substr, pre_ip):
            if n < 3:
                for l in range(1, 4):
                    if len(substr) > l:
                        if l > 1 and substr[0] == '0':
                            break
                        x = int(substr[:l])
                        if x <= 255:
                            ipaddr(n + 1, substr[l:], "{}{}.".format(pre_ip, x))
            else:
                if substr and int(substr) <= 255:
                    if len(substr) > 1 and substr[0] == '0':
                        return
                    ans.append("{}{}".format(pre_ip, int(substr)))
        
        ipaddr(0, s, "")
        return ans   
