# with open('note.csv', 'r') as f1, open('note.csv', 'w') as f2:
#     lines = f1.readlines()
#     for line in lines:
#         line = line.strip()
#         if line == 'искомая строка':
#             f2.write('новая строка\n')
#         else:
#             f2.write(line)

i = 2
str=""
with open('note.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.find(f"Заметка № {i}") != -1:
            index1 = line.find("Заголовок:")
            index2 = line.find("|", index1)
            for i in range(index1+11,index2-1):
                str = str + line[i]
            #line.replace(*)
        else:
            print("Заметка не найдена!!!")