# sum of numbers in a nested list
list = [14, [15, [16, 17], 18], 19]
sum=0
for i in list:
    if type(i) == int:
        sum+=i
    else:
        for j in i:
            if type(j)==int:
                sum+=j
            else:
                for k in j:
                    sum+=k
print(sum)
# find min and max values in nested list
list=[[1,2,3,1],[8,9,2,9],[11,55,12,24]]
for i in list:
    minNum=i[0]
    maxNum=i[0]
    for j in i:
        if maxNum<j:
            maxNum=j
        elif minNum>j:
            minNum=j
    print(minNum,maxNum)
#find the maximum and minimum numbers in a given list.
maxNum=list[0]
minNum=list[0]
for i in list:
    if type(i) == int:
        if i>maxNum:
            maxNum=i
        elif i<minNum:
            minNum=i
    else:
        for j in i:
            if type(j)==int:
                if j>maxNum:
                    maxNum=j
                elif j<minNum:
                    minNum=j
            else:
                for k in j:
                    if k>maxNum:
                        maxNum=k
                    elif k<minNum:
                        minNum=k
print(minNum,maxNum)

