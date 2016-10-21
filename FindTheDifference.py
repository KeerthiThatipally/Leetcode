class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_len = s.strip().__len__()
        t_len = t.strip().__len__()
        if (t_len == s_len + 1):
            s1 = 0
            t1 = 0
            for i in s:
                s1 = s1 + ord(i)

            for i in t:
                t1 = t1 + ord(i)

            r = t1 - s1

            return chr(r)
        else:
            return 0


if __name__=="__main__":
    sol=Solution()
    res=sol.findTheDifference(" ","y")
    print(res)