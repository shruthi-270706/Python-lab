def is_prime(n):
    if n < 2:return False
    for i in range(2, n):
        if n % i == 0:return False
    return True
def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
def number_analysis():
    numbers = []
    count = int(input("How many numbers will you enter? "))
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        if num > 0 and num not in numbers:
            numbers.append(num)
    with open("number_analysis.txt", "w") as f:
        for n in numbers:
            line = str(n) + ": "
            if n % 2 == 0:line += "even"
            else:line += "odd"
            if is_prime(n):line += ", prime"
            if is_perfect(n):line += ", perfect"
            f.write(line + "\n")
    print("Saved in number_analysis.txt")
def restore_text():
    text = input("Enter the scrambled paragraph: ")
    changed = ""
    for ch in text:
        if ch in 'aeiouAEIOU':changed += chr(ord(ch) + 1)
        else:changed += ch
    words = changed.split()
    final = ""
    for word in words:
        if len(word) == 5 and word.isalpha():final += word[::-1] + " "
        else:final += word + " "
    with open("ObfuscationReversal.txt", "w") as f:
        f.write(final.strip())
    print("Saved in ObfuscationReversal.txt")
def summary_report():
    text = input("Enter paragraph for summary: ")
    chars = [',', '.', '!', '?', ';', ':']
    for ch in chars: text = text.replace(ch, '')
    words = text.split()
    total = 0
    unique = []
    freq = {}
    longest = ""
    for word in words:
        total += 1
        if word not in unique:unique.append(word)
        if len(word) > len(longest):longest = word
        if word in freq:freq[word] += 1
        else:freq[word] = 1
    most = ""
    highest = 0
    for word in freq:
        if freq[word] > highest:
            highest = freq[word]
            most = word
    with open("summary.txt", "w") as f:
        f.write("Total words: " + str(total) + "\n")
        f.write("Unique words: " + str(len(unique)) + "\n")
        f.write("Longest word: " + longest + "\n")
        f.write("Most frequent word: " + most + " (" + str(highest) + " times)\n")
    print("Saved in summary.txt")
def pattern_matches():
    text = input("Enter text to find patterns: ")
    chars = [',', '.', '!', '?', ';', ':']
    for ch in chars:
        text = text.replace(ch, '')
    words = text.split()
    matched = []
    for word in words:
        small = word.lower()
        if small.startswith('a') or small.endswith('g'):
            if small not in matched:
                matched.append(small)
        elif 's' in small and 'i' in small and 't' in small:
            if small not in matched:
                matched.append(small)
    with open("pattern_matches.txt", "w") as f:
        for word in sorted(matched):
            f.write(word + "\n")
    print("Saved in pattern_matches.txt")
def palindrome():
    text = input("Enter text for palindrome check: ")
    chars = [',', '.', '!', '?', ';', ':']
    for ch in chars:
        text = text.replace(ch, '')
    words = text.split()
    found = []
    for word in words:
        word = word.lower()
        if len(word) >= 3 and word == word[::-1]:
            if word not in found:
                found.append(word)
    found.sort()
    with open("palindromes.txt", "w") as f:
        for w in found:
            f.write(w + "\n")
    print("Saved in palindromes.txt")
def keyword_index():
    text = input("Enter text to extract keywords: ")
    chars = [',', '.', '!', '?', ';', ':']
    for ch in chars:
        text = text.replace(ch, '')
    words = text.split()
    used = []
    freq = {}
    for w in words:
        small = w.lower()
        if len(small) > 4:
            if small not in used:
                used.append(small)
                freq[small] = 1
            else:freq[small]+= 1
    used.sort()
    with open("keywords.txt", "w") as f:
        for word in used:f.write(word+": " +str(freq[word])+"\n")
    print("Saved in keywords.txt")
while True:
    print("\n1:Number Analysis\n2:Text Restoration\n3:Summary Report")
    print("4:Pattern Match\n5:Palindromes\n6:Keywords\n7:Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:number_analysis()
    elif ch == 2:restore_text()
    elif ch == 3:summary_report()
    elif ch == 4:pattern_matches()
    elif ch == 5:palindrome()
    elif ch == 6:keyword_index()
    elif ch == 7:break