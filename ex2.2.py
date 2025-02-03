text = open(file="pg2701.txt", mode="r", encoding="UTF-8")
while 1:
    line = text.readline() 
    if line == "CHAPTER 1. Loomings.\n":
        break
    

vowels = []
wordcount = 0
for line in text:
    for word in line.split():
        vowels.append(0)
        for l in word:
            if l == 'a' or l == 'A' or l == 'e' or l == 'E' or l == 'i' or l == 'I' or l == 'o' or l == 'O' or l == 'u' or l == 'U' or l == 'y' or l == 'Y':
                vowels[wordcount] += 1
        wordcount += 1

print(wordcount)
print(sum(vowels)/wordcount)