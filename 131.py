s = "Programming"
unique_set = set(s)
vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
dis_vowels = unique_set.intersection(vowels)
count = len(dis_vowels)
print("Number of distinct vowels:", count)
print("Unique characters in the string:", unique_set)