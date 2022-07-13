def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(': stack.append(s[i])
            else:
                if len(stack)==0: return False
                p = stack[-1]
                if s[i]==']' and p!='[': return False
                elif s[i]=='}' and p!='{': return False
                elif s[i]==')' and p!='(': return False
                else: stack.pop()
        if len(stack)==0: return True
                
          
# Time: O(n)
# Space: O(n)
