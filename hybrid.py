with open("one_hundred.txt", "r") as file:
    data = file.read()
    # for num in data:
    #     line = int(num)

line = data.split()

numbers = [eval(i) for i in line]
print(numbers)

max_value = max(numbers)
min_value = min(numbers)

print(f"{max_value}, {min_value}")

for num in numbers:
    if num == range(min_value, max_value + 1):
        print(f"{num} is between 1-100")
    elif num != range(min_value, max_value + 1):
        print(f"{num} is not between 1-100")
