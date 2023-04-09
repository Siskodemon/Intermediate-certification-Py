import view_output
import moduls
import controller
import menu_view

def edit():
    number = view_output.select_note()
    view_output.select_message()
    chois = int(view_output.object_selection())
    if chois == 1:
        header = moduls.search_old_str(number,"Заголовок: ","|")
        with open('note.csv', 'r') as f1:
            lines = f1.readlines()
            str=[]
            for line in lines:
                line = line.strip()
                if line.find(f"Заметка № {number}") != -1:
                    new_header = view_output.insert_new_str()
                    str.append(line.replace(header,new_header,1)+"\n")
                else:
                    str.append(line + "\n")
        with open('note.csv', 'w') as f2:
            for line in str:
                f2.write(line)
    elif chois == 2:
        content = moduls.search_old_str(number, "Содержание:", ";")
        with open('note.csv', 'r') as f1:
            lines = f1.readlines()
            str = []
            for line in lines:
                line = line.strip()
                if line.find(f"Заметка № {number}") != -1:
                    new_content = view_output.insert_new_str()
                    str.append(line.replace(content, new_content, 1)+"\n")
                else:
                    str.append(line + "\n")
        with open('note.csv', 'w') as f2:
            for line in str:
                f2.write(line)
    else:
        print("Заметка не найдена!!!")
    menu_view.strat_menu()
    controller.action()
