s=input("Enter string:")
count = 0
# Defining a set with Vowels
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        # Incrementing the count if the vowel repeats
        count += 1
print("Count of the vowels is:")
# Prints the Vowel count
print(count)