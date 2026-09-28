print("Q1")
# Print the numbers from 1 to 50

for i in range(1, 51):
    print(i)

print()





print("Q2")
# Print the numbers from 0 to 50

for i in range(50,0,-1): #range(start , stop , step)

    print(i)
print()





print("Q3")
#Multiplication Table 

n= int(input("enter a number :"))
for k in range (1,11):
    print(n*k)




print("Q4")
#Sum of n natural number

n=7
sum= 0
for i in range (1, n+1):
    sum +=i
print("Total sum=" ,sum)

#OR


print("Q5")

n=8
sum=0
i=1
while i<=n:
    sum +=i

    i+=1
print(sum)


print("Q6")
#Factorial of 1st n natural number

n= int(input("enter a number:"))
fact=1 
i=1
while i<=n:
    fact *=i
    i+=1
print("Factorial of this number is=" , fact)




    #OR
print("Q7")

n=5
fact=1
for i in range(1, n+1):
    fact*=i
print("Factorial=" , fact)












