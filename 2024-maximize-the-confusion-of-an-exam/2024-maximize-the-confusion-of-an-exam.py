class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:


        
        l=0
        f_count=0
        t_count=0
        ans=0
        for r in range(len(answerKey)):
            if answerKey[r] =='T':
                t_count += 1
            else:
                f_count += 1
            while min(t_count , f_count)>k :
                if answerKey[l]=='T':
                    t_count-=1
                else:
                    f_count-=1
                l+=1
            ans=max(ans,r-l+1)

        return ans
        