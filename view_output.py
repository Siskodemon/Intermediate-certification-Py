def print_view_note_output():
    delimiter()
    print("Созданные заметки: ")

def delimiter():
    print("=====================================")

def create_not_output():
    print("-------------------------------------")
    print(f"Заметка успешно создана!!!")
    delimiter()

def error_output():
    print("Ошибка!Файл не найден!")
    delimiter()

def input_header():
    return input("Введите название заголовка заметки: ")

def input_content():
    return input("Введите содержание заметки: ")

def select_note():
    return input("Введите номер заметки: ")

def select_message():
    print("Введите \"1\" если редактируем заголовк или \"2\" если редактируем содержание...")

def object_selection():
    return input("--> ")

def insert_new_str():
    return input("Введите новое значение: ")
