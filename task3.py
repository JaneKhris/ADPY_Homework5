from task1 import logger


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

@logger
def add():
    number_new = input('Введите номер документа: ')
    type_new = input('Введите тип документа: ')
    name_new = input('Введите имя владельца документа: ')
    shelf_new = input('Введите номер полки для хранения: ')

    doc_new = {}
    doc_new["type"] = type_new
    doc_new["number"] = number_new
    doc_new["name"] = name_new

    documents.append(doc_new)

    directories.setdefault((shelf_new), [])
    directories[shelf_new].append(number_new)

@logger
def people(list):
    number = input('Введите номер документа для поиска: ')
    for document in list:
        if document["number"] == number:
            print(f'Владелец документа {document["name"]}')
            return
    print('Документ с введенным номером не найден')

@logger
def shelf(dict):
    number = input('Введите номер документа для поиска: ')
    for directory, doc_num in dict.items():
        if number in doc_num:
            print(f'Документ находится на {directory} полке')
            return
    print('Документ с введенным номером не найден')

@logger
def list_show(list_gen):
    for document in list_gen:
        str = ' '.join(list(document.values()))
        print(str)

@logger
def delete(list1, list2):
    number = input('Введите номер документа для удаления: ')
    for document in list1:
        if document["number"] == number:
            list1.remove(document)
            for directory, doc_num in list2.items():
                if number in doc_num:
                    doc_num.remove(number)
            return
    print('Документ с введенным номером не найден')


while True:
    comand = input('Введите команду: ')
    if comand == 'p':
        people(documents)
    elif comand == 's':
        shelf(directories)
    elif comand == 'l':
        list_show(documents)
    elif comand == 'a':
        add()
    elif comand == 'd':
        delete(documents, directories)
    elif comand == 'b':
        break
    else:
        print('Неверный ввод')


