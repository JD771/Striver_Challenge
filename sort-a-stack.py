def sortInsert(stack, ele):
        if len(stack)==0 or ele>stack[-1]:
            stack.append(ele)
        else:
            temp = stack.pop()
            sortInsert(stack, ele)
            stack.append(temp)
    if len(stack)!=0:
        temp = stack.pop()
        sortStack(stack)
        sortInsert(stack, temp)
    return stack

# Time: O(n^2)
# Space: O(n)
