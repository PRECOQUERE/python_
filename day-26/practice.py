numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
# print(new_list)

double_list = [n * 2 for n in range(1,4)]
# print(double_list)

names = ['Alex', 'Beth', 'caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)