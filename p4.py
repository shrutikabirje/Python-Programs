Question:-Given a string, return the sum and average of the digits that appear in the string, ignoring all other
characters
For Example: –
sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5



s=input("Enter the string with numbers")
sum = 0
count = 0
l=s.split()
for i in l:
    if i.isnumeric():
        sum += int(i)
        count +=1
print("Total Marks are: ", sum)
print("Percentage is: ", sum/count)
