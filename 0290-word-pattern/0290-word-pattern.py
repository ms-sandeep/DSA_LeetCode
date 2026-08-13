class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split()
        dic1={}
        dic2={}
        
        if len(s)!=len(pattern):
            return False
        else:
            for i in range(len(s)):
                ch=pattern[i]
                word=s[i]
                
                if ch in dic1 and dic1[ch]!=word:
                    return False
                if word in dic2 and dic2[word]!=ch:
                    return False
                dic1[ch]=word
                dic2[word]=ch
        return True
        