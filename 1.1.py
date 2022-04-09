#Display odd and even numbers between a given range
first_num=int(input("Enter the starting number: "))
last_num=int(input("Enter the last number: "))

print("Even numbers are:")
for i in range(first_num,last_num+1):
    if(i%2==0):
        print(i)

print("Odd numbers are:")
for i in range(first_num,last_num+1):
    if(i%2==1):
        print(i)