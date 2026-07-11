line='-'*40
integers=[]
index=[]
count=0
print(line)
print("Linear Search")
print(line,end='\n')
print("Enter 10 numbers:")
for i in range(10):
    integers.append(int(input()))
target=int(input("Enter Target value: "))
for ind,num in enumerate(integers):
    if(num==target):
        count+=1
        index.append(ind)
if(count>1):
    print(f"{target} found at indices: ",end='')
    for ind in index:
        print(ind,end=' ')
elif(count==1):
    print(f"{target} found at index: {index[0]}")
else:
    print("Not found")