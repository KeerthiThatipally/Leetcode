class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict={}
        if(s.strip().__len__()>0):

            var=False
            for i in s:

                if(myDict.__contains__(i)):
                    temp=myDict.get(i)

                    temp=temp+1
                    myDict.__setitem__(i,temp)
                else:
                    myDict.__setitem__(i,1)
            res = s.__len__()

            for i in myDict.keys():

                temp=myDict.get(i)


                if(temp==1):



                    for j in range(s.__len__()):
                        if(i==s[j]):
                            if(j<=res):
                                var=True
                                res=j

            if(var==True):
                return res
            else:
                return -1
        else:
            return -1













if __name__=="__main__":
    sol=Solution()
    res=sol.firstUniqChar("loveleetcode")
    print(res)