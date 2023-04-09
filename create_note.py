from datetime import datetime
import menu_view
import view_output
import moduls
import controller
import view_output

def input_note():
    view_output.delimiter()
    create(view_output.input_header(), view_output.input_content())

def create(name, content):
    try:
        with open('note.csv','a') as new_note:
            new_note.write(f"Заметка № {moduls.note_count()+1} | Создана: {datetime.now()} | Заголовок: {name} | Содержание: {content} ;\n")
            new_note.close()
            view_output.create_not_output()
    except Exception:
        view_output.error_output()
    menu_view.strat_menu()
    controller.action()
