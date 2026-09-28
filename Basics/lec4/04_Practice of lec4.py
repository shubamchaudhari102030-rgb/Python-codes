#WAP to enter marks of 3 subjects from user and store them in a dictionary , start with an empty dictionary.

marks = {}
x= int(input("enter phy :"))
marks.update({"phy" : x})

x= int(input("enter chem : "))
marks.update({"chem" : 96})

x= int(input("enter maths:"))
marks.update({"maths":  93})

print(marks)



#Figure out a way to store 9 & 9.0 as separate values in the set ( You can take help of built-in function)

#Method 1
values = { "9" , 9.0}
print(values)
print(type(values))


#Method 2
values = {
    ("float" , 9.0) , ("int" , 9)
}
print(values)
print(type(values))
