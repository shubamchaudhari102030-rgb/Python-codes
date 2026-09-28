#Recursive function.


def show(n):
    if(n==0):
        return  #return nhi lagate to negative value bhi print kar deta....
    print(n)
    show(n-1)


show(3)  #10,9,8,7,6,5,4,3,2,1

print("END")


print()

# factorial example

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(5))

