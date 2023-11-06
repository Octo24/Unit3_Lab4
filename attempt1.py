with open("Unit3_Lab4-1/one_hundred.txt", "r") as file:
    data = file.read()
    # for num in data:
    #     line = int(num)

line = data.split()
print(line)

allNumbers = list(range(1, 101))



number = [int(i) for i in line]

def findNumber(number):
    for num in number:
        if num in range(1, 100 + 1):
            print(f"{num} is between 1-100")
        else:
            print(f"{num} is NOT between 1-100")
        # elif num != range(1, 100 + 1):
        #     print(f"{num} is not between 1-100")

def missingNumbers(allNumbers, number):
    missingNumbers = list(set(allNumbers) - set(number))
    print(f"missing number {missingNumbers}")
    return missingNumbers

findNumber(number)
    
missingNumbers(allNumbers, number)


def my_own_sort(number):
    n = len(number)
     
    # Bubble Sort
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
                swapped = True
        if (swapped == False):
            break
 
my_own_sort(number)


with open("Unit3_Lab4-1/one_hundred_sorted.txt", "w") as file:
  
    for num in number:
        file.write(str(num) + ", ")



        



# numbers = []

# for line in data:
#     num = line.strip("\n").split(",")
#     numbers.append(num)

# print(num)
# print(numbers)




