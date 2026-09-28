nums = [1,2,3,4,5]
for val in nums:
    print(val)




#Search for a number x in this touple using loop
#(1,4,9,16,25,36,49,64,81,100,49)

nums= (1,4,9,16,25,36,49,64,81,100,49)
x=49
idx = 0
for el in nums:
    if(el==x):
        print("number found at idx" , idx)
    idx +=1
 