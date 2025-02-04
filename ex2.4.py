import timeit

# Read the file content once
with open('pg2701.txt', mode='r', encoding='utf-8') as file:
    text = []
    while True:
        line = file.readline()
        if line == "CHAPTER 1. Loomings.\n":
            break
    text = file.readlines()

# Function to compute the average number of vowels
def compute_average_vowels():
    vowels = []
    wordcount = 0
    for line in text:
        for word in line.split():
            vowels.append(0)
            for l in word:
                if l in 'aeiouAEIOUyY':
                    vowels[wordcount] += 1
            wordcount += 1
    return sum(vowels) / wordcount if wordcount != 0 else 0

# Timing the function 100 times
times = timeit.repeat(stmt=compute_average_vowels, repeat=100, number=1)

# Printing the average time across 100 repetitions
average_time = sum(times) / len(times)
print(f'Average computation time: {average_time} seconds')
