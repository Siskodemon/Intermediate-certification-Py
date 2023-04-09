import menu_view
import controller
import view_output

def output_notes():
    view_output.print_view_note_output()
    with open('note.csv', 'r') as note:
        for i in note.readlines():
            print(i)
        note.close()
    view_output.delimiter()
    menu_view.strat_menu()
    controller.action()

