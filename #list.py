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



