# read Input
my_file = open("input.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")

# Part 1
idx_list = [idx + 1 for idx, val in enumerate(data_into_list) if val == '']
calories =  [data_into_list[i: j] for i, j in zip([0] + idx_list, idx_list + ([len(data_into_list)] if idx_list[-1] != len(data_into_list) else []))]
calories_per_elf = []

for i in range(0,len(calories)):
    while("" in calories[i]):
        calories[i].remove("")
    for x in range(0,len(calories[i])):
        calories[i][x] = int(calories[i][x])
    calories_per_elf.append(sum(calories[i]))

sorted_elfs_by_calories = sorted(calories_per_elf)
print("Result_1: " + str(sorted_elfs_by_calories[-1]))


# Part 2
last_3 = sorted_elfs_by_calories[-1]+sorted_elfs_by_calories[-2]+sorted_elfs_by_calories[-3]
print("Result_2: "+ str(last_3))
