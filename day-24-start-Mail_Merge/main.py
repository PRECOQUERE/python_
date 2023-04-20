# file = open("day-24-start\myfile.txt") 
# content = file.read()
# print(content)
# file.close()

# #with open("day-24-start\myfile.txt", mode='w') as file: 읽기모드
# with open("day-24-start\myfile.txt") as file:
#     content = file.read()
# print(content)

# with open("day-24-start\myfile.txt", mode='w') as file:
#     # All reset and write
#     file.write("nex text.")

# # mode = 'a' => append
# with open("day-24-start\myfile.txt", mode='a') as file:
#     file.write("\nNext Text.")

# 경로 붙여넣었을 때, 오류 발생시 '\' => '/'로 변경해주면 됨.
with open("day-24-start/New_file.txt", mode='w') as file:
    file.write("Next Text.")    