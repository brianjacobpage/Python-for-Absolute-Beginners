#create a tuple var and print the value of each element with position
myTuple = (1, 2, "pie", "apple", "47Ronnin", (16 * 16))

for i in myTuple:
    print (myTuple.index(i), i)

#Tuples require a comma after an element, even when there is only 1 element, IE myTuple = (100,)
#except in the case of the last element in a tuple with multiple elements. IE myTuple = (100, 200)
#you can nest tuples within tuples
#tuples are immutable, where as lists are mutable