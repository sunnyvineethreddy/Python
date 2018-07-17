# importing Counter to print the count the words
from collections import Counter
t = str(input("Enter the text"))
# Sorts the words  and splits the line
myWords=sorted(t.split())
# Arrange  the words as in dictionary
myList=dict(Counter(myWords))
print(myList)

