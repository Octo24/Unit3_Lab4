with open("one_hundred.txt", "r") as file:
    data = file.read()
    # for num in data:
    #     line = int(num)

line = data.split()
print(line)


number = [eval(i) for i in line]
for num in number:
    if num == range(1, 100 + 1):
        print(f"{num} is between 1-100")
    elif num != range(1, 100 + 1):
        print(f"{num} is not between 1-100")

# def my_own_sort():


        



# numbers = []

# for line in data:
#     num = line.strip("\n").split(",")
#     numbers.append(num)

# print(num)
# print(numbers)




