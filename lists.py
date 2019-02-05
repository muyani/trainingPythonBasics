# list = ["bike","bike","cricket","travel bag",2,"drawers","bed","suitcase"]
#
# print (list)
#
# # length of a list
# print(len(list))
# #get the first item in a list
# print (list[0])
# # add an item in a list
# list.append("bed")
# print (list)
# #remove an item from a list
# list.remove('bed')
# print("after remove",list)
# # count items in a list
# print ("counted bike",list.count("bike"))

myNumbers = [3,4,7,1,1]
# # find the minimum and maximum numbers in a list
# print(max(myNumbers))
# print (min(myNumbers))


greatest = 0
for i in myNumbers:
    if i > greatest:
        greatest = i
print ("our greatest number is ",greatest)

# clear the whole list
myNumbers.clear()
print(myNumbers)
#ASSIGNMENT: use an if statement and a for loop to find the smallest number in a list.