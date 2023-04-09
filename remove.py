import view_output
import controller
import menu_view

def remove():
    number = view_output.select_note()
    with open('note.csv', 'r') as f1:
        lines = f1.readlines()
        str = []
        for line in lines:
            line = line.strip()
            if line.find(f"Заметка № {number}") == -1:
                str.append(line + "\n")
    with open('note.csv', 'w') as f2:
        for line in str:
            f2.write(line)
    menu_view.strat_menu()
    controller.action()
