a= {1,2,2,2, "hello" , "world" , 8}   #or  a= set([21,4,5,7,4,5,"hello])
print(a)
print(type(a))

#Set Methods


a= {3,1,54}
a.add(7) #adds 7 in last , and rest are automatically in ascending order
print(a)

a= {25,6,4,5,7,4}
a.remove(4) #removes both 4 and converts in ascending order
print(a)

a={4,6,3,6,8,982,6}
a.clear()
print(a) # Empties the set


a= {8,94,8,4,7,4,3,2,6,3}
a.pop()
print(a)



a= {1,2,3,4,5,6}
b= {4,5,6,7,8,9,0}

print(a.union(b)) # returns 0,1,2,3,4,5,6,7,8,9
print(a.intersection(b)) #returns 4,5,6