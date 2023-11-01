f = open("one_hundred.txt") 
# f = open("sample.txt") 

max_value = ""
min_value = "99999"

for line in f:
    if len(line) > 1:
        list_nums = line.split()
        for num in list_nums:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num
print(f"max: {max_value}, min: {min_value}")


for line in f:
    if len(line) > 1:
        list_nums = line.split()
        for num in list_nums:
            for r in range(min_value, max_value):
                if r == num:
                    print(f"{r} not present")

# for line in f:
#     if len(line) > 1:
#         list_nums = line.split()
#         for num in list_nums:



# for num in line:
#     if num in range(1, 100 + 1)