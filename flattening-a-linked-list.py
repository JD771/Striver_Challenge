def mergelists(a, b):
    fh = None
    ft = None
    while a!= None and b != None:
        if fh is None:
            if a.data<b.data:
                fh = a
                ft = a
                a = a.bottom
            else:
                fh = b
                ft = b
                b = b.bottom
        else:
            if a.data< b.data:
                ft.bottom = a
                a= a.bottom
                ft = ft.bottom
            else:
                ft.bottom = b
                b = b.bottom
                ft = ft.bottom
    if a:
        ft.bottom = a
    if b:
        ft.bottom = b
    return fh

def flatten(root):
    #Your code here
    if root== None or root.next == None:
        return root
    root.next = flatten(root.next)
    root = mergelists(root, root.next)
    return root
# Time: O(n)
# Space: O(1)
