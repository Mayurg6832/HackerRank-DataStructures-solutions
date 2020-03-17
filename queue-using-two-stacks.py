stack1=[]
stack2=[]
for i in range(int(input())):
    lst=list(map(int,input().split()))
    if lst[0]==1:
        stack1.append(lst[-1])
        stack2.append(stack1.pop())
    elif lst[0]==2:
        stack2.pop(0)
    elif lst[0]==3:
        print(stack2[0])
