#write a function to print length of a list

cities=["delhi" , "washim" , "pune" , "Mumbai" , "Nagpur"]

def a(list):
    print(len(list))

print(len(cities))  #or ...   a(cities)

print(cities[3])


#Find the factorial

n=5
def calc_fact(n):
    fact=1

    for i in range(1, n+1):
        fact *=i
        
    print(fact)

calc_fact(5)  #output nahi print hot ahe , dabal try karjo



#wAF to convert USD To IND

def converter(usd_val):

    inr_val= usd_val*90

    print(usd_val, "USD=" , inr_val, "INR")

converter(3)




  #Check the given number is easy or odd 


def check_for(n):
    if n%2==0:
        print("Even number")

    else:
        print("Odd Number")

check_for(6)


#use recursive function for calculating sum of n natural numbers 

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) + n 


sum= calc_sum(6)
print(sum)



#write a recursive function to print all elements in a list

def print_list(list, idx=0):
    if(idx==len(list)):
        return

    print(list[idx])
    print_list(list , idx +1)

fruits=["mango", "banana" , "grapes"]

print_list(fruits)

    

















