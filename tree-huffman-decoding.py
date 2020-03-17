def decodeHuff(root, s):
    #Enter Your Code Here
    result=""
    current=root
    for i in s:
        if int(i)==0:
            current=current.left
        else:
            current=current.right
        if current.left==None and current.right==None:
            result+=current.data
            current=root
    print(result)
