class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s =""
        for ch in s:
          if ch.isalnum():
              new_s += ch.lower()
       
        reverse = new_s[::-1]
        if new_s == reverse:
             return True
        else:
              return False    
            
        
                
