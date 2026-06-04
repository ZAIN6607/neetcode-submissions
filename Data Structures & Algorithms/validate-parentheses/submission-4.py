class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        o="[{("
        close="]})"
        pairs = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in o:
                stack.append(c)
            if c in close and len(stack)==0:

                
                return False  
            if c in close and stack[-1]!=pairs[c]:
                return False 
            if c in close and len(stack)!=0 and stack[-1]==pairs[c]:
                stack.pop()
           
        if(len(stack)==0):
            return True
        else:
            return False    
                
                    



          


        


        