#list
#rule: should run it one step at a time
Friends =["sopheak", "many", "mony", "dalin", "dano"]
#print all
print(Friends)
#print by index
print(Friends[0]) #the first one
print(Friends[-1]) # print from right to left, index start with -1
print(Friends[1:]) #will output the element from 1
print(Friends[1:3]) #will output from index 1 until 2

#add two lists
numbers =[2,5,7,4,2]
Friends =["sopheak", "many", "mony", "dalin", "dano"]
Friends.extend(numbers) #add two list together
print(Friends)

#append the lists
Friends.append("Vireak")
print(Friends)

#insert inside the list
Friends.insert(3,"MOLIKA")
print(Friends)

#remove any element
Friends.remove("dano")
print(Friends)

#remove everything from the list
Friends.clear()
print(Friends)

#POP the element, to get rid of the last element inside the list
list=["sopheak", "many", "mony", "dalin", "dano", "dano","dano"]
list.pop() #we can't pop from an empty list
print(list)

#check whether element is in hte list
print(list.index("mony")) #show the element according to its index
# print(Friends.index("Mike"))

#count how many time the element show up insid the list.
print(list.count("dano"))

#short the list in ascending order, by the num or the alphabet
list.sort()
print(list)

#reverse the list
list.reverse()
print(list)

#copy the list
list2 = list.copy()


