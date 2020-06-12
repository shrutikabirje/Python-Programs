Question:Arrange String characters such that lowercase letters should come first
Given input String of combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first.



s=input("enter the string")
s1=""
lower = []
upper = []
for i in s:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
print(s1.join(lower+upper))
