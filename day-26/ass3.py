with open('day-26/ass3_1.txt') as file1 :
    file1_ = file1.readlines()

with open('day-26/ass3_2.txt') as file2 :
    file2_ = file2.readlines()

result = [int(num) for num in file1_ if num in file2_]
# Write your code above 👆

print(result)