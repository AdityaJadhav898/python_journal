#Print all the numbers between 100 to 200 which are divisible by 4 and 7
num1=100
num2=200

print("Number div by 4 and 7 btw 100 to 200 are:")
for i in range(num1,num2+1):
    if((i%4==0) and (i%7==0)):
        print(i)