Question:Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.


s1=input("enter the string1")
s2=input("enter the string2")
a=int(len(s1)/2)
print(a)
b=[s1[0:a-1]+s2+s1[a-1:]]
print(b)
