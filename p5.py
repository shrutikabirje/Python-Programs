Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

l1= [3, 6, 9, 12, 15, 18, 21]
l2= [4, 8, 12, 16, 20, 24, 28]
l3= []

odd=l1[1::2]
print("Elements at odd-index from list one")
print(odd)

even= l2[0::2]
print("Element at even-index from list two")
print(even)

print("Printing Final third list")
l3.extend(odd)
l3.extend(even)
print(l3)

