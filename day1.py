
file = open('day1.txt', 'r')
lines = file.readlines()

num_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }

total = 0

for line in lines:
    index_to_nums = {}

    for n in num_words.keys():
        ind = line.find(n)
        while ind != -1:
            index_to_nums[ind] = num_words[n] 
            ind = line.find(n, ind + 1)

    for j in range(len(line)):
        if line[j].isnumeric():
            index_to_nums[j] = line[j] 
            break

    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            index_to_nums[i] = line[i] 
            break
    
    min_i = min(index_to_nums.keys())
    max_i = max(index_to_nums.keys())

    num = index_to_nums[min_i] + index_to_nums[max_i]
    
    total += int(num)

print(total)