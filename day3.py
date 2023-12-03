
file = open('day3.txt', 'r')
lines = file.readlines()

total = 0

rows = []
nums = []

row_counter = 0
for line in lines:
    line = line.strip()
    rows.append(list(line))

    cur_num = ''
    for c_ind in range(len(line)):
        if line[c_ind].isnumeric():
            cur_num += line[c_ind]
        else:
            if cur_num != '':
                nums.append((int(cur_num), row_counter, c_ind - len(cur_num)))
                cur_num = ''

    if cur_num != '':
        nums.append((int(cur_num), row_counter, len(line) - len(cur_num)))      
        cur_num = ''

    row_counter += 1

for num in nums:
    n = num[0]
    row = num[1]
    col = num[2]

    cur_col = col

    end_col_ind = col + (len(str(n)) - 1)

    found_sym = False
    while cur_col <= end_col_ind:

        # behind
        if cur_col == col and cur_col - 1 >= 0:
            val = rows[row][cur_col - 1]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # bottom left
        if cur_col == col and cur_col - 1 >= 0 and row + 1 < len(rows):
            val = rows[row + 1][cur_col - 1]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # top left
        if cur_col == col and cur_col - 1 >= 0 and row - 1 >= 0:
            val = rows[row - 1][cur_col - 1]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # front
        if cur_col == end_col_ind and cur_col + 1 < len(rows[row]):
            val = rows[row][cur_col + 1]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # bottom right
        if cur_col == end_col_ind and cur_col + 1 < len(rows[row]) and row + 1 < len(rows):
            val = rows[row + 1][cur_col + 1]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # top right
        if cur_col == end_col_ind and cur_col + 1 < len(rows[row]) and row - 1 >= 0:
            val = rows[row - 1][cur_col + 1]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # top
        if row - 1 >= 0:
            val = rows[row - 1][cur_col]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        # bottom
        if row + 1 < len(rows):
            val = rows[row + 1][cur_col]
            if  val != '.' and not val.isnumeric():
                found_sym = True
                break

        cur_col += 1

    if found_sym:
        total += n

print(total)

