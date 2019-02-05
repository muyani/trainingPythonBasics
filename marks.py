maths = int(input("Enter your Mathematics results: "))
english = int(input("Enter your English results: "))
kiswahili = int(input("Enter your Kiswahili results: "))
socialStudies = int(input("Enter your Social Studies results: "))
science = int(input("Enter your Science results: "))

a,b,c,d,e = maths,english,kiswahili,socialStudies,science

total = a+b+c+d+e

average = total/5

if average >= 80:
    print("Grade A")
elif average >= 70 and average < 80:
    print ("Grade B")
elif average >= 60 and average < 70:
    print("Grade C")
elif average >=50 and average < 60:
    print("Grade D")
else:
    print ("Fail")

print (total)


# Nested if
# a kid







