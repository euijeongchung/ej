s = "abcbcd"
longest = ""
for i in range(len(s)):
    sub = s[i]
    index = i
    while index + 1 < len(s):
        if s[index + 1] >= s[index]:
            sub += s[index + 1]
            index += 1
        else:
            break
    if (len(sub) > len(longest)):
        longest = sub
print("Longest substring in alphabetical order is: " + longest)