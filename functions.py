# sum = 1+1
# A function is a bunch of code you create so that you use it somewhere else

# function definition
def likhwu(string):
    print (string)


# calling a function
likhwu("hamza")


#reusing that function.
likhwu(1+1)

igcse = [85,76,76,89,50,42]

# create a function to calculate total marks
def calculateTotal(marks):
    sum = 0
    for i in marks:
        sum += i
    return sum

# use the above function to calculate my marks for igcse
total = calculateTotal(igcse)
print(total)




