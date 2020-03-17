stack=[]
maxi=[]
for i in range(int(input())):
    lst=list(map(int,input().split()))
    if lst[0]==1:
        stack.append(lst[-1])
        if not maxi or lst[-1]>=maxi[-1]:
            maxi.append(lst[-1])
    elif lst[0]==2:
        ele=stack.pop()
        if ele==maxi[-1]:
            maxi.pop()
    elif lst[0]==3:
        print(maxi[-1])
