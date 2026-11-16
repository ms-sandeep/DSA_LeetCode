class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        max_val=0
        vowel="aeiou"
        count=0

        if len(s)==1 and s in vowel:
            return 1
        
        if len(s)==1 and s not in vowel:
            return 0
        
        for i in range(k):
            if s[i] in vowel:
                count+=1

        max_val=count

        for i in range(k,len(s)):
            if s[i] in vowel:
                count+=1
            
            if s[i-k] in vowel:
                count-=1
        
            max_val=max(count, max_val)

        return max_val

            

        
            
            

        