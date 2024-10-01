class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=len(s)
        for i in range(0,l):
            if i<l//2:
                temp=s[i]
                s[i]=s[l-1-i]
                s[l-1-i]=temp

        
