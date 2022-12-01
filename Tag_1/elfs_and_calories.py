# read Input
my_file = open("input.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")

# Part 1

size = len(data_into_list)
idx_list = [idx + 1 for idx, val in enumerate(data_into_list) if val == '']
calories =  [data_into_list[i: j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]
calories_per_elf = []

for i in range(0,len(calories)):
    while("" in calories[i]):
        calories[i].remove("")
    for x in range(0,len(calories[i])):
        calories[i][x] = int(calories[i][x])

    calories_per_elf.append(sum(calories[i]))

d = {"elf_"+str(i): calories_per_elf[i] for i in range(1,len(calories_per_elf)) }




sorted_elfs_by_calories = sorted(d.items(), key=lambda x:x[1])
print(sorted_elfs_by_calories)


# Part 2
x = 70374 + 68996 + 65240
print(x)



# temp_idx = test_list.index('')
# res = [test_list[: temp_idx], test_list[temp_idx + 1: ]]