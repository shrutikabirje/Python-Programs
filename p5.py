Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

l1= [3, 6, 9, 12, 15, 18, 21]
l2= [4, 8, 12, 16, 20, 24, 28]
l3= []
l4=[]
l5=[]
for i in range (len(l1)):
    if i%2!=0:
        l3.append(l1[i])
print("odd elements in list 1:",l3)
for j in range (len(l2)):
    if j%2==0:
        l4.append(l2[j])
print("even elements in list 2:",l4)
l5=(l3+l4)
print("Final list:",l5)

