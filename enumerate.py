names=["Alice","bob","John"]
for i in range(len(names)):
    print(f"name{i}is {names[i]}")
    
    
for i,name in enumerate(names):
   print(f"name {i} is {name}")
    

ar=[]
n = input("Enter array size: ")
arrayNums=input("Enter array elements separated by commas :")
for i in range(n):
     numbers = int(input().split(","))
     ar.append(numbers)
print("Sum:", sum(ar))