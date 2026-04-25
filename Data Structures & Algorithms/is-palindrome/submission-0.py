class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123546789"
        word=""
        word1=s.lower()
        ac=""
        for x in word1:
            if x in alphabets.lower() or x in alphabets and x!=" ":
                word+=x
    
        print(word,word[::-1])
        return word==word[::-1]