sum=0.0
n=int(input("Enter the numbers of elements: "))
print(f"Enter {n} numbers: ")
for i in range(n):
    num=float(input())
    sum+=num
print(f"The sum of {n} numbers is {sum} ")