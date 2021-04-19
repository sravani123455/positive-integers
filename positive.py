list1= []
n=7
print("enter the values:")
for i in range(n):
    data= int(input())
    list1.append(data)
for num in list1:
    if num>=0:
        print(num)
