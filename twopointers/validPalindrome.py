import re 

class Palindrome:
    #Without using regular expression or in built function such as isalnum. 
    def valid_palindrome(self,s):
        i=0 
        j= len(s)-1
        
        #O(n) Time complexity 
        while(i<j):
            while i<j and not self.isAlphaNum(s[i]):
                i+=1
            while j>i and not self.isAlphaNum(s[j]):
                j-=1
            if s[i].lower()!=s[j].lower():
                return False 

            i+=1
            j-=1
            
        return True
        
    def isAlphaNum(self,c):
        #O(1) SC 
        return(ord('A') <= ord(c) <=ord('Z') or
        ord('a') <= ord(c) <=ord('z') or
        ord('0') <= ord(c) <=ord('9'))
        
    
p= Palindrome()
print(p.valid_palindrome("Was it a car or a cat I saw?"))
print(p.valid_palindrome("tab a cat"))