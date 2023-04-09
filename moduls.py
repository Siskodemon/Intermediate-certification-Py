import view_output

def note_count():
    try:
        count = 0
        with open('note.csv', 'r') as note:
            for i in note.readlines():
                count += 1
        note.close
        return count
    except Exception:
        view_output.error_output()

def search_old_str(index, index_begin, index_end):
    str = ""
    with open('note.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(f"Заметка № {index}") != -1:
                index1 = line.find(index_begin)
                index2 = line.find(index_end, index1)
                for i in range(index1+11, index2-1):
                    str = str + line[i]
                # line.replace(*)
    return str
    