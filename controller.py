import create_note
import menu_view
import view_notes
import edit_note
import view_output
import remove

def action():
    i = int (view_output.object_selection())
    if i == 1:
        create_note.input_note()
    elif i == 2:
        view_notes.output_notes()
    elif i == 3:
        edit_note.edit()
    elif i == 4:
        remove.remove()
    else: print("Выход")
