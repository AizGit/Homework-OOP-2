f1 = open ('1.txt', 'r', encoding='utf-8')
f2 = open ('2.txt', 'r', encoding='utf-8')
f3 = open ('3.txt', 'r', encoding='utf-8')
lines = []
with open('1.txt', 'r', encoding='utf-8') as my_file_1:
  file_contents_1 = my_file_1.read()
with open('2.txt', 'r', encoding='utf-8') as my_file_2:
  file_contents_2 = my_file_2.read()
with open('3.txt','r', encoding='utf-8') as my_file_3:
  file_contents_3 = my_file_3.read()
print(file_contents_1)
print(file_contents_2)
print(file_contents_3)
